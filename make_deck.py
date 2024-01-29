import pandas as pd
import os 

def make_pronunciation_file(word):
	word = "hello"
	command = f"say --file-format=WAVE --data-format=alaw -o 'audio/{word}.wav' {word}"
	os.system(command)

def main():	
	"""
	- concatenate each deck
	- remove duplicate italian words
	- send each word to 'say' command and output aiff
		say -v 'Emma' -o "audio/${word}.aiff" "${word}" 
	"""
	pass

if __name__ == "__main__":
	main()
