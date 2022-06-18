import json

from typing import Union

from termcolor import colored # TODO don't use a lib and put ANSI escaped by hand maybe?

_EQUIVALENTS = {
	"dark_red" : "red",
	"red" : "red",
	"gold": "yellow",
	"yellow": "yellow",
	"dark_green": "green",
	"green": "green",
	"aqua": "cyan",
	"dark_aqua": "cyan",
	"dark_blue": "blue",
	"blue": "blue",
	"light_purple": "magenta",
	"dark_purple": "magenta",
	"white": "white",
	"gray": "grey",
	"dark_gray": "grey",
	"black": "white"
}

def _parse_formatted_block(msg:dict) -> str:
	attr = []
	txt = msg["text"] if "text" in msg else msg["translate"] if "translate" in msg else "N/A"
	if "bold" in msg and msg["bold"]:
		attr.append("bold")
	if "underlined" in msg and msg["underlined"]:
		attr.append("underline")
	if "obfuscated" in msg and msg["obfuscated"]:
		attr.append("blink")
	if "color" in msg:
		return colored(txt, _EQUIVALENTS[msg["color"]], attrs=attr)
	else:
		return colored(txt, "white", attrs=attr)

def parse_chat(msg:Union[dict,str], ansi_color:bool=False) -> str:
	"""Recursive function to parse minecraft chat json, with optional colors"""
	if isinstance(msg, dict):
		data = msg
	elif isinstance(msg, str):
		try:
			data = json.loads(msg)
		except ValueError:
			return str(msg) # It's not json, it's already plaintext
	else:
		return str(msg)
	out = ""
	if "text" in data or "translate" in data:
		if ansi_color:
			out += _parse_formatted_block(data)
		elif "text" in data:
			out += data["text"]
		elif "translate" in data:
			out += data["translate"]
	if "with" in data:
		for elem in data["with"]:
			out += parse_chat(elem, ansi_color)
	if "extra" in data:
		for elem in data["extra"]:
			out += parse_chat(elem, ansi_color)
	return out

def format_item(item:dict, compact=False, nbt:bool=False) -> str:
	if not item:
		return "[   ]"
	item_id = f"{item['id']:03d}"
	item_count = f"{item['count']}x" if item['count'] > 1 else ''
	item_damage = f"|{item['damage']:03d}" if 'damage' in item else ''
	item_nbt = str(item['nbt']) if item['nbt'] else ''
	if compact:
		return f"[{item_id:03d}]"
	if nbt:
		return f"[{item_count}{item_id}{item_damage}]({item_nbt})"
	return f"[{item_count}{item_id}{item_damage}]"

