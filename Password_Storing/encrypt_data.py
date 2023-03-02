# // Imports \\ #
from cryptography.fernet import Fernet
import os
import load_key
import load_path
import decrypt_data
import encrypt_data

# // Encrypt File Function \\ #
def encrypt_data():
	try:
		key = load_key.load_key()
		key.decode('ascii')
		f = Fernet(key)
		path = load_path.load_path()
		with open(path, 'rb') as enc_file:
			original = enc_file.read()
		encrypted = f.encrypt(original)
		with open(path, 'wb') as encrypted_file:
			encrypted_file.write(encrypted)
		enc_file.close()
		encrypted_file.close()
	except Exception as e:
		print(c(f"[ENCRYPT_DATA] ERROR: {e}", "red"))