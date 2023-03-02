# // Imports \\ #
from cryptography.fernet import Fernet

def load_path():

	return open("./program_information/usr_path.enc", 'r').read()