from termcolor import colored

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

def parse_chat(msg:dict, color:bool=True) -> str:
	"""Recursive function to parse minecraft chat json, with optional colors"""
	out = ""
	if "text" in msg:
		if color:
			out += _parse_formatted_block(msg)
		else:
			out += msg["text"]
	if "with" in msg:
		for elem in msg["with"]:
			out += parse_chat(elem, color)
	if "extra" in msg:
		for elem in msg["extra"]:
			out += parse_chat(elem, color)
	return out
