
import os

from parsers import (GODOT_PATTERN, NODE_PATTERN, get_strings_from_json,
                     get_strings_from_src)


def get_strings_folder(path, exclude=[]):
	strings = []
	path_size = len(path)
	for root, subdirs, files in os.walk(path):
		is_excluded = [
			root.startswith(excluded)
			for excluded in exclude
		]
		if True not in is_excluded:
			for filename in files:
				ext = os.path.splitext(filename)[1]
				complete_path = "{}/{}".format(root,filename)
				relative_path = complete_path[path_size:]
				new_strings = []
				if ext == ".gd":
					new_strings = get_strings_from_src(complete_path, GODOT_PATTERN)
				elif ext ==".tscn":
					new_strings = get_strings_from_src(complete_path, NODE_PATTERN)
				elif ext ==".json":
					new_strings = get_strings_from_json(complete_path)
				strings.extend([
					text.get_simple_text(relative_path)
					for text in new_strings
				])

	return strings
