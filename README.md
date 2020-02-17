# Godot Extract Texts

Suported files:
* __tscn__: It will extract all the texts in scenes .tscn (Is looking for the text property of elements)
* __gd__:It will extract all the texts from godot that are calling to tr method
* __json__:It will extract all texts or text list inside keys "text" of a json file

Output files:
* Generate a .pot file with all founded texts as msgid and msgstr empty
* [optional] Generate a .po file with all founded text as msgid and msgstr.

## Usage

```
python3 main.py path_to_project_folder output_file.pot
```

See the help:
```
Process .tscn, .gd and .json files to extract texts

positional arguments:
  src                   Root source folder of the godot project
  template_file         File .pot to generate

optional arguments:
  -h, --help            show this help message and exit
  -e EXCLUDE, --exclude EXCLUDE
                        Folders to exclude in the searc
  --po PO_FILE          generate a .po file
```


## Sample output

```
# File some_path/some_file.tscn line: 23 column: 12
msgid "the text from code"
msgstr ""
```
