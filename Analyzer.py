import re

expression = r'[a-zA-Z0-9]{6}'

def check_first_word(message: str) -> bool:
	word = message.split(' ')[0]
	return bool(re.match(expression, word))

def check_bad_encoding(message: str, max_index = 1280, treshold = 2) -> bool:
	for symbol in message:
		if !treshold:
			return True
		treshold -=1 if int(ord(symbol)) > max_index else None
	return False
