# // Imports \\ #
from cryptography.fernet import Fernet
import os
from termcolor import colored

# \\ Variables // #
c = colored

# \\ Write Key Function // #
def write_key():
	try:
		print(c("[!!!] Generating Key...", "blue"))
		os.system("sleep 3")
		key = Fernet.generate_key()
		key.decode('ascii')
		with open("./program_information/key.key", 'wb') as key_file:
			key_file.write(key)
			key_file.close()
	except Exception as e:
		print(c(f"[WRITE_KEY] ERROR: {e}", "red"))