# Godot Extract Texts

* It will extract all the texts in scenes .tscn (Is looking for the text property of elements)
* It will extract all the texts from godot that are calling to tr method

## Usage

```
python3 main.py path_to_folder output_file.pot
```



## Sample output

```
# File some_path/some_file.tscn line: 23 column: 12
msgid "the text from code"
msgstr ""
```
