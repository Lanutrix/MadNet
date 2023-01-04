from cryptography.fernet import Fernet
import os
from base64 import b64encode, b64decode


def write_key(keyname):
    # Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open(f'{keyname}.key', 'wb') as key_file:
        key_file.write(key)


def encrypt(filename, key):
    # Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Читаем файл
        data = file.read()
    encrypted_data = f.encrypt(data)
    encrypted_data_b64 = b64encode(encrypted_data)
    with open(filename, 'w') as file:
        file.write(encrypted_data_b64.decode('windows-1251'))


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        _for_decryption = file.read()
    decoded_encrypted_data = b64decode(_for_decryption)
    for_write = f.decrypt(decoded_encrypted_data).decode('windows-1251')

    with open(filename, 'w') as f:
        f.write(for_write)


keyname = 'crypt'
# загрузить ключ
if os.path.exists(f'{keyname}.key'):
    key = open(f'{keyname}.key', 'rb').read()
else:
    write_key(keyname)
# имя шифруемого файла
file = 'huh.py'
# зашифровать файл
encrypt(file, key)

# расшифровать файл
decrypt(file, key)
