from cryptography.fernet import Fernet

with open("Key", 'wb') as f:
	f.write(Fernet.generate_key())
	print("[+] saved to Key")