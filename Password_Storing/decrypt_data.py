# // Imports \\ #
from cryptography.fernet import Fernet
import os
import load_key
import load_path

# // Decrypt Data Function \\ #
def decrypt_data():
	try:
		key = load_key.load_key()
		key.decode('ascii')
		f = Fernet(key)
		path = load_path.load_path()
		with open(path, 'rb') as enc_file:
			original = enc_file.read()
		decrypted = f.decrypt(original)
		with open(path, 'wb') as decrypted_file:
			decrypted_file.write(decrypted)
		enc_file.close()
		decrypted_file.close()
	except Exception as e:
		print(c(f"[DECRYPT_DATA] ERROR: {e}", "red"))
