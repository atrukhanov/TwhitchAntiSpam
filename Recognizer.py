from Analyzer import check_first_word, check_bad_encoding

class Recognizer(object):

	def __init__(self, channel: str):
		self.__channel = channel
		self.__message_buffer = []
		self.__message_flags = []

	def check_message(self,  message: str) -> bool:
		return check_message(message) and check_bad_encoding(message)

	def push_buffer(self, message):
		self.__message_buffer.append(message)
		self.__message_flags.append(False)

	def check_matching(self, message: str):
		for i in range(len(self.__message_buffer)):
			if self.__message_buffer[i][6:] == message[6:]:
				return i
		return -1

	def get_message(self, id: int):
		return self.__message_buffer[id]

	def check_flag(self, id: int) -> bool:
		return self.__message_flags[id]

	def set_ban(self, id: int):
		self.__message_flags[id] = True
