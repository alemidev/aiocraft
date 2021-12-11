#!/usr/bin/env python
import os
import json
import keyword
import logging

from pathlib import Path
from typing import Tuple, List, Dict, Union, Set, Type as Class

from aiocraft.mc.types import *

# TODO de-spaghetti this file sometime!

DIR_MAP = {"toClient": "clientbound", "toServer": "serverbound"}
PREFACE = """\"\"\"[!] This file is autogenerated\"\"\"\n\n"""
IMPORTS = """from typing import Tuple, List, Dict, Union
from ....packet import Packet
from ....types import *\n"""
IMPORT_ALL = """__all__ = [\n\t{all}\n]\n"""
REGISTRY_ENTRY = """
REGISTRY = {entries}\n"""
OBJECT = """
class {name}(Packet):
	__slots__ = {slots}
	{fields}

	_state : int = {state}

	_ids : Dict[int, int] = {ids}
	_definitions : Dict[int, List[Tuple[str, Type]]] = {definitions}
"""

class Ref:
	name : str
	args : tuple

	def __equals__(self, other) -> bool:
		if self.args:
			return self.name == other.name and self.args == other.args
		return self.name == other.name

	def __init__(self, name:str, *args):
		self.name = name or "anon"
		self.args = args

	def __repr__(self) -> str:
		if self.args:
			out = self.name + "("
			for arg in self.args:
				out += repr(arg) + ", "
			out += ")"
			return out
		return self.name

TYPE_MAP = {
	"varint": Ref('VarInt'),
	"u8": Ref('Byte'),
	"i8": Ref('Byte'),
	"u16": Ref('UnsignedShort'),
	"u32": Ref('UnsignedInt'),
	"u64": Ref('UnsignedLong'),
	"i16": Ref('Short'),
	"i32": Ref('Int'),
	"i64": Ref('Long'),
	"f32": Ref('Float'),
	"f64": Ref('Double'),
	"bool": Ref('Boolean'),
	"UUID": Ref('UUID'),
	"string": Ref('String'),
	"nbt": Ref('NBTTag'),
	"slot": Ref('Slot'),
	"position": Ref('Position'),
	"entityMetadataItem": Ref('EntityMetadataItem'),
	"entityMetadata": Ref('EntityMetadata'),
	"void": Ref('Void'),
}

HINT_MAP = {
	"varint": 'int',
	"u8": 'int',
	"i8": 'int',
	"u16": 'int',
	"u32": 'int',
	"u64": 'int',
	"i16": 'int',
	"i32": 'int',
	"i64": 'int',
	"f32": 'float',
	"f64": 'float',
	"bool": 'bool',
	"UUID": 'str',
	"string": 'str',
	"nbt": 'bytes',
	"slot": 'dict',
	"position": 'tuple',
	"entityMetadataItem": 'bytes',
	"entityMetadata": 'bytes',
}

def _format_line(i, depth:int=0) -> str:
	nl = ('\n' if depth > 0 else " ")
	tab = '\t' * depth
	return nl + tab + \
		f",{nl}{tab}".join(f"{repr(e)}" for e in i) + \
		nl + ('\t' * (depth-1))

def format_dict(d:dict, depth:int=1) -> str:
	return "{" + _format_line((Ref(f"{k} : {v}") for k,v in sorted(d.items())), depth) + "}"

def format_list(l:list, depth:int=0) -> str:
	return "[" + _format_line(l, depth) + "]"

def format_tuple(l:list, depth:int=0) -> str:
	return "(" + _format_line(l, depth) + ")"

def mctype(slot_type:Any) -> Ref:
	if isinstance(slot_type, str) and slot_type in TYPE_MAP:
		return TYPE_MAP[slot_type]
	if isinstance(slot_type, list):
		t = slot_type[0]
		v = slot_type[1]
		if t == "buffer": # Array of bytes
			if "countType" in v and v["countType"] == "integer":
				return Ref('IntegerByteArray')
			return Ref('ByteArray')
		elif t == "array": # Generic array
			return Ref('ArrayType',
				mctype(v["type"]),
				(v["count"] if "count" in v else mctype(v["countType"]) if "countType" in v else Ref('VarInt'))
			)
		elif t == "container": # Struct
			return Ref('StructType', Ref(", ".join(format_tuple((p["name"], mctype(p["type"]))) for p in v if "name" in p))) # some fields are anonymous???
		elif t == "option": # Optional
			return Ref('OptionalType', mctype(v))
		elif t == "switch": # Union
			return Ref('SwitchType',
				v["compareTo"].split('/')[-1],
				Ref(format_dict({int(k) if k.isnumeric() else repr(k):mctype(x) for k,x in v["fields"].items()}, depth=0)),
				mctype(v["default"]) if "default" in v and v['default'] != 'void' else None,
			)
			# return SwitchType(mctype(v)) # TODO
		elif t == "bitfield":
			return Ref('Int')
		# elif t == "mapper": # ????
		# 	return TrailingData
		else:
			logging.error("Encountered unknown composite data type : %s", t)
	return Ref('TrailingData')

def mchint(slot_type:Any) -> Ref:
	if isinstance(slot_type, str) and slot_type in HINT_MAP:
		return Ref(HINT_MAP[slot_type])
	if isinstance(slot_type, list):
		t = slot_type[0]
		if t == "buffer": # Array of bytes
			return Ref('bytes')
		elif t == "array": # Generic array
			return Ref('list')
		elif t == "container": # Struct
			return Ref('dict')
		elif t == "option": # Optional
			return Ref('tuple')
		elif t == "switch": # Union
			return Ref('bytes')
			# return SwitchType(mctype(v)) # TODO
		# elif t == "mapper": # ????
		# 	return TrailingData
	return Ref('bytes')

def pytype(t:list) -> str:
	vals = set(str(x) for x in t)
	if len(vals) <= 1:
		return next(iter(vals))
	return 'Union[' + ','.join(x for x in vals) + ']'

def snake_to_camel(name:str) -> str:
	return "".join(x.capitalize() for x in name.split("_"))

# def parse_slot(slot: dict) -> str:
# 	name = slot["name"] if "name" in slot else "anon"
# 	if keyword.iskeyword(name):
# 		name = "is_" + name
# 	t = mctype(slot["type"] if "type" in slot else "restBuffer")
# 	return f"(\"{name}\", {t.__name__})"
# 
# def parse_field(slot: dict) -> str:
# 	name = slot["name"] if "name" in slot else "anon"
# 	if keyword.iskeyword(name):
# 		name = "is_" + name
# 	t = mctype(slot["type"] if "type" in slot else "restBuffer")
# 	return f"{name} : {t._pytype.__name__}"

class PacketClassWriter:
	name  : str
	attrs : Set[str]
	types : Dict[str, List[Type]]
	hints : Dict[str, List[Type]]
	ids   : Dict[int, int]
	definitions : Dict[int, List[Tuple[str, Type]]]
	state : int

	def __init__(self, pkt:dict, state:int):
		self.name = pkt["name"]
		self.state = state
		self.attrs = set()
		self.ids = {}
		self.types = {}
		self.hints = {}
		self.definitions = {}
		for v, defn in pkt["definitions"].items():
			self.ids[v] = defn["id"]
			self.definitions[v] = []
			for field in defn["slots"]:
				if "name" not in field:
					logging.error("Skipping anonymous field %s", str(field))
					continue
				field_name = field["name"] if not keyword.iskeyword(field["name"]) else "is_" + field["name"]
				self.attrs.add(field_name)
				self.definitions[v].append((field_name, mctype(field["type"])))
				if field_name not in self.types:
					self.types[field_name] = set()
				self.types[field_name].add(mctype(field["type"]))
				if field_name not in self.hints:
					self.hints[field_name] = set()
				self.hints[field_name].add(mchint(field["type"]))

	def compile(self) -> str:
		return PREFACE + \
			IMPORTS + \
			OBJECT.format(
				name=self.name, 
				ids=format_dict(self.ids, depth=2), 
				definitions=format_dict({ k : Ref(format_list(Ref(format_tuple(x)) for x in v)) for k,v in self.definitions.items() }, depth=2),
				slots=format_tuple(["id"] + list(self.attrs), depth=0), # TODO jank fix when no slots
				fields="\n\t" + "\n\t".join(f"{a} : {pytype(self.hints[a])}" for a in self.attrs),
				state=self.state,
			)

class RegistryClassWriter:
	registry : dict

	def __init__(self, registry:dict):
		self.registry = registry

	def compile(self) -> str:
		return REGISTRY_ENTRY.format(
			entries='{\n\t' + ",\n\t".join((
				str(v) + " : { " + ", ".join(
					f"{pid}:{clazz}" for (pid, clazz) in self.registry[v].items()
				) + ' }' ) for v in self.registry.keys()
			) + '\n}'
		)

def _make_module(path:Path, contents:dict):
	os.mkdir(path)
	imports = ""
	for key, value in contents.items():
		imports += f"from .{key} import {value}\n"
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

		# Build data structure containing all packets with all their definitions for different versions
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

				for v, defn in pkt["definitions"].items():
					if v not in registry:
						registry[v] = {}
					registry[v][defn['id']] = snake_to_camel(packet)

				with open(mc_path / f"proto/{state}/{direction}/{packet}.py", "w") as f:
					f.write(PacketClassWriter(pkt, _STATE_MAP[state]).compile())

			with open(mc_path / f"proto/{state}/{direction}/__init__.py", "a") as f:
				f.write(RegistryClassWriter(registry).compile())

if __name__ == "__main__":
	compile()





