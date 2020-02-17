#!/bin/env python
import argparse
import json
import os

from find import get_strings_folder
from models import MSG_FILE, MSG_MESSAGE_DATA, MSG_TEMPLATE_DATA, MsgId


def process_matchs(data_list):
	trans_hash = {}
	trans_list = []
	for match in data_list:
		msgid = match[0]
		trans = trans_hash.get(msgid, None)
		if not trans:
			trans = MsgId(json.dumps(msgid))
			trans_hash[msgid] = trans
			trans_list.append(trans)
		trans.add_location(match[1], match[2], match[3])

	trans_list.sort(key=lambda t: t.msg)
	return trans_list

def generate_file(file, trans_list, template):
	texts_list = [
		trans.get_str(template)
		for trans in trans_list
	]

	with open(file, 'w') as f:
		f.write(MSG_FILE.format("\n".join(texts_list)))

def run(options):
	strings_list =  get_strings_folder(options.src, options.exclude)

	texts_list = process_matchs(strings_list)

	generate_file(options.template_file, texts_list, MSG_TEMPLATE_DATA)
	if options.po is not None:
		generate_file(options.po, texts_list, MSG_MESSAGE_DATA)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Process .tscn, .gd and .json files to extract texts")

	parser.add_argument("-e", "--exclude", action='append', default=[], help="Folders to exclude in the searc")
	parser.add_argument('--po', help='generate a .po file', default=None)
	parser.add_argument('src', help='Root source folder of the godot project')
	parser.add_argument('template_file', help="File .pot to generate")

	args = parser.parse_args()
	run(args)
