import json
import re

from models import FileText

NEW_LINE_PATTERN = re.compile("\r\n|\r|\n")
GODOT_PATTERN = re.compile('[ \.(]tr\(([\"\'].*?)\)')
NODE_PATTERN = re.compile('text.*=.*([\"\'].*[\"\'])')


def extract_strings_from_json( keys_list, data, path):
	strings = []
	if isinstance(data, dict):
		for key in data.keys():
			value = data[key]
			if key in keys_list:
				plain_path = ".".join(path)
				if isinstance(value,list):
					strings.extend([
						FileText(text, plain_path+".{}[{}]".format(key, idx))
						for idx, text in enumerate(value)
						if isinstance(text, str)
					])
				elif isinstance(value, str):
					strings.append(FileText(value, plain_path))
			else:
				strings.extend(extract_strings_from_json(keys_list, value, path+[key]))
	elif isinstance(data, list):
		key=""
		if len(path)>0:
			key = path.pop()
		for idx, value in enumerate(data):
			strings.extend(extract_strings_from_json(keys_list, value, path+["{}[{}]".format(key, idx)]))
	return strings

def get_strings_from_json(filename):
	with open(filename, 'r') as f:
		data = json.load(f)
		return extract_strings_from_json("text", data, [])


def get_strings_from_src(filename, regex):
	list_strings = []
	with open(filename, 'r') as f:
		contents = f.read()
		match = regex.search(contents)
		while match is not None:
			start = match.start()
			new_lines = NEW_LINE_PATTERN.split(contents[:start])
			translation = FileText(
				eval(match.group(1)),
				len(new_lines),
				len(new_lines[-1])
			)
			list_strings.append(translation)
			contents = contents[match.end():]
			match = regex.search(contents)
	return list_strings
