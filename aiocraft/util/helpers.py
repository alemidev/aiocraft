import json

from typing import Union, List

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

def _parse_formatted_block(text: str, msg:dict) -> str:
	attr = []
	if "bold" in msg and msg["bold"]:
		attr.append("bold")
	if "underlined" in msg and msg["underlined"]:
		attr.append("underline")
	if "obfuscated" in msg and msg["obfuscated"]:
		attr.append("blink")
	if "color" in msg:
		return colored(text, _EQUIVALENTS[msg["color"]], attrs=attr)
	else:
		return colored(text, "white", attrs=attr)

def _parse_translated_block(translate:str, withs: List[dict]) -> str:
	out = ""
	if translate == "chat.type.text":
		out += "<"
		out += parse_chat(withs[0])
		out += "> "
		out += parse_chat(withs[1])
	else: # fallback behavior
		out += translate + "("
		for elem in withs:
			out += parse_chat(elem) + ","
		out += ")"
	return out

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

	if "translate" in data and "with" in data:
		translation = _parse_translated_block(data["translate"], data["with"])
		if ansi_color:
			out += _parse_formatted_block(translation, data)
		else:
			out += translation
	if "text" in data:
		if ansi_color:
			out += _parse_formatted_block(data["text"], data)
		else:
			out += data["text"]
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

