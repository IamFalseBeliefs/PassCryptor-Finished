# // Imports \\ #
from cryptography.fernet import Fernet
import os
import load_key
import load_path
import encrypt_data
import decrypt_data
from termcolor import colored

# \\ Variables // #
c = colored

# // Add Data to File Function \ #
def add_data():
	try:
		key = load_key.load_key()
		f = Fernet(key)
		path = load_path.load_path()
		data_to_add = input(c("[+] Syntax: reason:username:password: [DATA]: ", 'green')).encode('utf-8')
		with open(path, 'ab') as data:
			data.write(data_to_add)
			data.write(b";")
			data.close()
	except Exception as e:
		print(c(f"[ADD_DATA] ERROR: {e}", "red"))