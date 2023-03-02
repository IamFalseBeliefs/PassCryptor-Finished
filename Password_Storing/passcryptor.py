# // Imports \\ #
# \\ CUSTOM  // #
import write_key
import load_key
import encrypt_data
import decrypt_data
import add_data
import load_path

# // Premade \\ #
from cryptography.fernet import Fernet
import os
from termcolor import colored

# \\ Variables // #
c = colored

# // Main Function \\ #
def main():
	os.system("clear") # WINDOWS os.system("cls")
	try:
		print(c("		    ____                  ______                 __              ", 'red'))
		print(c("		   / __ \\____ ___________/ ____/______  ______  / /_____  _____   ", 'white'))
		print(c("		  / /_/ / __ `/ ___/ ___/ /   / ___/ / / / __ \\/ __/ __ \\/ ___/  ", 'blue'))
		print(c("		 / ____/ /_/ (__  |__  ) /___/ /  / /_/ / /_/ / /_/ /_/ / /        ", 'green'))
		print(c("		/_/    \\__,_/____/____/\\____/_/   \\__, / .___/\\__/\\____/_/    ", 'red'))     
		print(c("		                                 /____/_/                          ", 'magenta'))
		print(c("		<------ Password Encryption via File by FalseBeliefs ------>       ", 'yellow'))
		print(c("[1] Add Data To File", 'magenta'))
		print(c("[2] Decrypt and Read File", 'magenta'))
		print(c("[99] Exit :/", 'magenta'))
		sel = int(input(c("[SELECTION]: ", 'green')))
		if sel == 1:
			print(c("[!!!] Decrypting File...", 'blue'))
			os.system("sleep 3")
			decrypt_data.decrypt_data()
			add_data.add_data()
			print(c("[!!!] Re-encrypting File...", 'blue'))
			os.system("sleep 3")
			encrypt_data.encrypt_data()
			os.system("clear") # WINDOWS os.system("cls")
			main()
		elif sel == 2:
			print(c("[!!!] Loading key...", 'blue'))
			os.system("sleep 3")
			key = load_key.load_key()
			key.decode('ascii')
			print(c("[!!!] Loading Path...", 'blue'))
			os.system("sleep 3")
			path = load_path.load_path()
			print(c("[!!!] Decrypting File...", 'blue'))
			os.system("sleep 3")
			decrypt_data.decrypt_data()
			with open(path, 'rb') as enc_file:
				decrypted_data = enc_file.read()
			print(c("[!!!] Writing Decrypted File...", 'blue'))
			os.system("sleep 3")
			with open("./decrypted_file/enc.log", 'wb') as dec_file: # Decrypted path location
				dec_file.write(decrypted_data)
			dec_file.close()
			enc_file.close()
			print(c("[!!!] Re-encrypting File...", 'blue'))
			os.system("sleep 3")
			encrypt_data.encrypt_data()
			os.system("clear") # WINDOWS os.system("cls")
			main()
		else:
			print(c("THANK YOU FOR USING PASSCRYPTOR! HAVE A WONDERFUL DAY.", "red"))
			os._exit(0)
	except Exception as e:
		print(c(f"[passcryptor Main] ERROR: {e}", "red"))


# // Run Once Function \\ #
def once():
	try:
		with open("./program_information/ecno.nur", 'r') as run_once:
			if_ran = run_once.read()
		if if_ran == "29688":
			run_once.close()
			main()
		elif if_ran != "29688":
			print(c("[X] Input File Directory to Save Encryption to: ", "green"))
			usr_path = input(c("[PATH]: ", "green"))
			with open("./program_information/usr_path.enc", 'w') as path_file:
				path_file.write(usr_path)
				path_file.close()
			with open("./program_information/ecno.nur", 'w') as once_ran:
				once_ran.write("29688")
				once_ran.close()
			with open("./encrypted_file/enc.log", 'wb') as enc_file:
				write_key.write_key()
				print(c("[!!!] Writing Key To File", 'blue'))
				os.system("sleep 3")
				key = load_key.load_key()
				f = Fernet(key)
				tmp_data = f.encrypt(b":")
				enc_file.write(tmp_data)
				enc_file.close()
				os.system("clear") # WINDOWS os.system("cls")
			main()
	except Exception as e:
		print(c(f"[passcryptor Once] ERROR: {e}", "red"))
once()