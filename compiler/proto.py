#!/usr/bin/env python
import os
import json
import keyword
import logging

from pathlib import Path
from typing import List, Dict, Union

from aiocraft.mc.mctypes import *

DIR_MAP = {"toClient": "clientbound", "toServer": "serverbound"}
PREFACE = """\"\"\"[!] This file is autogenerated\"\"\"\n\n"""
IMPORTS = """from typing import Tuple, List, Dict
from ....packet import Packet
from ....mctypes import *\n"""
IMPORT_ALL = """__all__ = [\n\t{all}\n]\n"""
REGISTRY_ENTRY = """
REGISTRY = {entries}\n"""
OBJECT = """
class {name}(Packet):
	{fields}

	_state : int = {state}

	_ids : Dict[int, int] = {ids}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {slots}
"""

TYPE_MAP = {
	"varint": VarInt,
	"u8": Byte,
	"i8": Byte,
	"u16": UnsignedShort,
	"u32": UnsignedInt,
	"u64": UnsignedLong,
	"i16": Short,
	"i32": Int,
	"i64": Long,
	"f32": Float,
	"f64": Double,
	"bool": Boolean,
	"UUID": UUID,
	"string": String,
	"nbt": NBTTag,
	"slot": Slot,
	"position": Position,
	"entityMetadataItem": EntityMetadataItem,
	"entityMetadata": EntityMetadata,
}

def mctype(slot_type:Any) -> Type:
	if isinstance(slot_type, str) and slot_type in TYPE_MAP:
		return TYPE_MAP[slot_type]
	if isinstance(slot_type, list):
		name = slot_type[0]
		if name == "buffer":
			if "countType" in slot_type[1] and slot_type[1]["countType"] == "integer":
				return IntegerByteArray
			return ByteArray
		# TODO composite data types
	return TrailingByteArray

def snake_to_camel(name:str) -> str:
	return "".join(x.capitalize() for x in name.split("_"))

def parse_slot(slot: dict) -> str:
	name = slot["name"] if "name" in slot else "anon"
	if keyword.iskeyword(name):
		name = "is_" + name
	t = mctype(slot["type"] if "type" in slot else "restBuffer")
	return f"(\"{name}\", {t.__name__})"

def parse_field(slot: dict) -> str:
	name = slot["name"] if "name" in slot else "anon"
	if keyword.iskeyword(name):
		name = "is_" + name
	t = mctype(slot["type"] if "type" in slot else "restBuffer")
	return f"{name} : {t._pytype.__name__}"

class PacketClassWriter:
	title : str
	ids   : str
	slots : str
	fields: str
	state : int


	def __init__(self, title:str, ids:str, slots:str, fields:str, state:int):
		self.title = title
		self.ids = ids
		self.slots = slots
		self.fields = fields
		self.state = state

	def compile(self) -> str:
		return PREFACE + \
			IMPORTS + \
			OBJECT.format(
				name=self.title, 
				ids='{\n\t\t' + ',\n\t\t'.join(self.ids) + '\n\t}\n', 
				slots=self.slots,
				fields=self.fields,
				state=self.state,
			)

def _make_module(path:Path, contents:dict):
	os.mkdir(path)
	imports = ""
	for key in contents:
		imports += f"from .{key} import {contents[key]}\n"
	with open(path / "__init__.py", "w") as f:
		f.write(PREFACE + imports)

def compile():
	import shutil
	import zipfile
	from urllib.request import urlretrieve

	base_path = Path(os.getcwd())
	mc_path = base_path / 'aiocraft' / 'mc'

	# Retrieve proto definitions from PrismarineJS/minecraft-data
	urlretrieve("https://github.com/PrismarineJS/minecraft-data/zipball/master", mc_path / "minecraft-data.zip")

	with zipfile.ZipFile(mc_path / 'minecraft-data.zip', 'r') as f:
		f.extractall(mc_path)

	# First folder starting with PrismarineJS
	folder_name = next(folder for folder in os.listdir(mc_path) if folder.startswith("PrismarineJS"))

	shutil.rmtree(mc_path / 'proto')

	PACKETS = {
		"handshaking": {
			"clientbound": {},
			"serverbound": {},
		},
		"status": {
			"clientbound": {},
			"serverbound": {},
		},
		"login": {
			"clientbound": {},
			"serverbound": {},
		},
		"play": {
			"clientbound": {},
			"serverbound": {},
		}
	}
	
	# TODO load all versions!
	all_versions = os.listdir(mc_path / f'{folder_name}/data/pc/')
	all_versions.remove("common")
	all_proto_numbers = []
	# _make_module(mc_path / 'proto', { f"v{v.replace('.', '_').replace('-', '_')}":"*" for v in all_versions })

	for v in all_versions:
		if v == "0.30c":
			continue # Proto just too antique!
		if not os.path.isfile(mc_path / f'{folder_name}/data/pc/{v}/protocol.json') \
		or not os.path.isfile(mc_path / f'{folder_name}/data/pc/{v}/version.json'):
			continue
		with open(mc_path / f'{folder_name}/data/pc/{v}/version.json') as f:
			proto_version = json.load(f)['version']
		all_proto_numbers.append(proto_version)

		with open(mc_path / f'{folder_name}/data/pc/{v}/protocol.json') as f:
			data = json.load(f)

		for state in ("handshaking", "status", "login", "play"):
			for _direction in ("toClient", "toServer"):
				direction = DIR_MAP[_direction]
				try:
					buf = data[state][_direction]["types"]["packet"][1][0]["type"][1]["mappings"]
				except KeyError:
					logging.exception("Exception building %s|%s|%s definitions", v, state, direction)
					print("Exception building %s|%s|%s definitions" % (v, state, direction))
					# _make_module(mc_path / f"proto/{version}/{state}/{direction}", {})
					continue
				registry = { f"packet_{value}" : int(key, 16) for (key, value) in buf.items() }
				for p_name in data[state][_direction]["types"].keys():
					if p_name == "packet":
						continue # it's the registry entry
					if p_name not in registry:
						logging.warning("Trying to make definitions for packet '%s'", p_name)
						continue # wtf!
					packet = data[state][_direction]["types"][p_name]
					pid = registry[p_name]
					class_name = snake_to_camel(p_name)
					if p_name not in PACKETS[state][direction]:
						PACKETS[state][direction][p_name] = {
							"name" : class_name,
							"definitions" : {},
						}
					PACKETS[state][direction][p_name]["definitions"][proto_version] = {
						"id": pid,
						"slots" : packet[1],
					}

	_STATE_MAP = {"handshaking": 0, "status":1, "login":2, "play":3}

	_make_module(mc_path / 'proto', { k:"*" for k in PACKETS.keys() })
	for state in PACKETS.keys():
		_make_module(mc_path / f"proto/{state}", { k:"*" for k in PACKETS[state].keys() })
		for direction in PACKETS[state].keys():
			registry = {}
			_make_module(mc_path / f"proto/{state}/{direction}", { k:snake_to_camel(k) for k in PACKETS[state][direction].keys() })
			for packet in PACKETS[state][direction].keys():
				pkt = PACKETS[state][direction][packet]
				slots = []
				fields = set()
				ids = []
				for v in sorted(PACKETS[state][direction][packet]["definitions"].keys()):
					defn = pkt["definitions"][v]
					if v not in registry:
						registry[v] = {}
					registry[v][defn['id']] = snake_to_camel(packet)
					ids.append(f"{v} : 0x{defn['id']:02X}")
					v_slots = []
					v_fields = []
					for slot in defn["slots"]:
						v_slots.append(parse_slot(slot))
						fields.add(parse_field(slot))
					slots.append(f"{v} : [ {','.join(v_slots)} ],")

				with open(mc_path / f"proto/{state}/{direction}/{packet}.py", "w") as f:
					f.write(
						PacketClassWriter(
							pkt["name"],
							ids,
							'{\n\t\t' + '\n\t\t'.join(slots) + '\n\t}\n',
							'\n\t'.join(fields),
							_STATE_MAP[state]
						).compile()
					)

			with open(mc_path / f"proto/{state}/{direction}/__init__.py", "a") as f, open("/home/alemi/REGISTRY", "a") as fdbg:
				buf = ( # TODO make this thing actually readable, maybe not using nested joins and generators
					REGISTRY_ENTRY.format(
						entries='{\n\t' + ",\n\t".join((
							str(v) + " : { " + ", ".join(
								f"{pid}:{clazz}" for (pid, clazz) in registry[v].items()
							) + ' }' ) for v in registry.keys()
						) + '\n}'
					)
				)
				f.write(buf)
				fdbg.write(buf)





