
# -*- coding: utf8 -*-
from datetime import datetime
import os
from cryptography.fernet import Fernet


class Logger_Bot:
    def __init__(self) -> None:
        self.hh = ''
        self.dump = 'dump/'
        self.path = 'logs/'
        day = 3
        if not os.path.exists(self.dump):
            os.mkdir(self.dump)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        current, dirs, files = os.walk(self.path).__next__()
        if len(files) >= day:
            files = sorted(files)[:-3]
            for i in files:
                os.remove(self.path + i)

    def __save_log(self, text: str):

        name_file = self.path + 'log_' + datetime.now().strftime('%Y-%m-%d').replace(' ',
                                                                                     '_').replace(':', '-') + ".txt"

        if os.path.exists(name_file):

            with open(name_file, 'rb') as file:
                data2 = file.read()  # прочитали

            key = data2[:22] + data2[-22:]  # чтение ключа

            f = Fernet(key)

            dt = f.decrypt(data2[22:-22]).decode() + text
            data3 = key[:22] + f.encrypt(dt.encode()) + key[-22:]

            with open(name_file, 'wb') as new_log:
                new_log.write(data3)

        else:

            key = Fernet.generate_key()  # генер ключа шифрования
            f = Fernet(key)
            encrypted_text = key[:22] + key[-22:]

            with open(name_file, 'wb') as file:
                file.write(key[:22] + f.encrypt(encrypted_text) + key[-22:])

            self.__save_log('&#Logs&#')
            self.__save_log(text)

    def log(self, name_func, e_text):
        time_e = datetime.now().strftime('%H:%M:%S').replace(' ', '_').replace(':', '-')
        text = f"[{time_e}] {name_func}: {e_text}.&#"
        self.__save_log(text)

    def get_log(self, name_file):
        try:
            with open(self.path + name_file, 'rb') as file:
                data2 = file.read()
            key = data2[:22] + data2[-22:]  # чтение ключа
            f = Fernet(key)

            with open(self.path + name_file, 'rb') as file:
                data3 = file.read()[22:-22]

            data3 = f.decrypt(data3).decode().replace("&#", "\n")
            print(data3)
            with open(self.dump+name_file, 'w') as file:
                file.write(data3)
            return self.dump+name_file

        except:
            return False