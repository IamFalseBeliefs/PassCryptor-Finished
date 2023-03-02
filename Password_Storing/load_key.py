# // Imports \\ #
from cryptography.fernet import Fernet

# // Load Key Function \\ #
def load_key():
	return open("./program_information/key.key", 'rb').read()