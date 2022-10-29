import json
import threading
from time import sleep
import pyautogui as pag
import requests
import telebot

class Stirring():
    def __init__(self) -> None:
        self.n = 0

    def save(self):
        while 1:
            
            if self.white != []:
                id = pag.confirm(f"Сохранить?", "BDB")
                if id == 'OK':
                    outp = {
                            "name_pc"   : self.name,
                            "bot_token" : self.token,
                            "white_list": self.white,
                            
                            "info"      : "https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/documentation.txt",
                            "update"    : 0
                        }
                    with open("config.json", 'w', encoding='utf-8') as f:
                        json.dump(outp, f)
                        
                    exit()
            else:
              sleep(5)  
    def get_name(self):
        while True:
            name = pag.prompt("Укажите имя", "BDB")
            if name != '' and name != None:
                self.name = name
                break
    def get_token(self):
        while True:
            self.token = pag.prompt("Укажите токен", "BDB")
            if self.token != '' and self.token != None:
                
                link = f"https://api.telegram.org/bot{self.token}/getMe"
                d = requests.get(link).json()
                if d['ok']:
                    self.bot=telebot.TeleBot(self.token)
                    pag.alert("Отправте сообщение боту")
                    break
                else:
                    pag.alert("Вы указали неверный токен")
            else:
                    pag.alert("Вы указали неверный токен")
    def Run(self):
        self.white = []
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            if message.chat.type == 'private':
                id = pag.confirm(f"Ваше имя: {message.chat.first_name}\nUsername: {message.chat.username}", "BDB")
            elif message.chat.type == 'group':
                id = pag.confirm(f"Тип: группа\nНазвание: {message.chat.title}", "BDB")
            if id == 'OK':
                self.white.append(message.chat.id)
            self.bot.send_message(message.chat.id, f"Привет")
            
        @self.bot.message_handler(content_types=['text', 'photo', 'video'])
        def infokigb(message):
            if message.chat.type == 'private':
                id = pag.confirm(f"Ваше имя: {message.chat.first_name}\nUsername: {message.chat.username}", "BDB")
            elif message.chat.type == 'group':
                id = pag.confirm(f"Тип: группа\nНазвание: {message.chat.title}", "BDB")
            if id == 'OK':
                self.white.append(message.chat.id)
            self.bot.send_message(message.chat.id, f"Привет")
                
        self.bot.polling()


st = Stirring()
st.get_name()
st.get_token()
threading.Thread(target=st.save, args=()).start()
st.Run()
