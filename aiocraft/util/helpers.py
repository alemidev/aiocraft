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
	if "bold" in msg and msg["bold"]:
		attr.append("bold")
	if "underlined" in msg and msg["underlined"]:
		attr.append("underline")
	if "obfuscated" in msg and msg["obfuscated"]:
		attr.append("blink")
	if "color" in msg:
		return colored(msg["text"], _EQUIVALENTS[msg["color"]], attrs=attr)
	else:
		return colored(msg["text"], "white", attrs=attr)

def parse_chat(msg:Union[dict,str], ansi_color:bool=False) -> str:
	"""Recursive function to parse minecraft chat json, with optional colors"""
	if isinstance(msg, str):
		try:
			data = json.loads(msg)
		except ValueError:
			return str(msg) # It's not json, it's already plaintext
	else:
		data = msg
	out = ""
	if "text" in data:
		if ansi_color:
			out += _parse_formatted_block(data)
		else:
			out += data["text"]
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
	item_count = f"x{item['count']}" if 'count' in item else ''
	item_damage = f"|{item['damage']:03d}" if 'damage' in item else ''
	item_nbt = item['nbt'].pretty() if 'nbt' in item else ''
	if compact:
		return f"[{item_id:03d}]"
	if nbt:
		return f"[{item_id}{item_count}{item_damage}]({item_nbt})"
	return f"[{item_id}{item_count}{item_damage}]"

