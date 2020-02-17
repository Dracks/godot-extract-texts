import collections

MSG_LINE_COMMENT = "# file: {0} line: {1} column: {2}"
MSG_TEMPLATE_DATA = """{0}
msgid {1}
msgstr ""
"""

MSG_MESSAGE_DATA = """{0}
msgid {1}
msgstr {1}
"""

MSG_FILE = """
msgid ""
msgstr ""

{}
"""

class FileText:
	def __init__(self, msg, line, column=""):
		self.msg = msg
		self.line = line
		self.column = column

	def get_simple_text(self, filename):
		return TranslationTextSimple(self.msg, filename, self.line, self.column)

TranslationTextSimple = collections.namedtuple('TranslationTextSimple', ['text', 'file', 'line', 'column'])

class MsgId:
	def __init__(self, msg):
		self.msg = msg
		self.locations = []

	def add_location(self, filename, line, column):
		self.locations.append((filename, line, column))

	def get_str(self, template):
		comments = [
			MSG_LINE_COMMENT.format(*loc).strip()
			for loc in self.locations
		]
		return template.format("\n".join(comments), self.msg)
