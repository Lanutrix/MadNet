# -*- coding: utf8 -*-
import platform
import subprocess, os, re, time
import requests
import wget as wg
import pyautogui,os,time
import keyboard

opa_pc=0

def lock():
	scrnW, scrnH = pyautogui.size() # Get the size of the primary monitor.

	# while 1:
	currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
	print(currentMouseX,currentMouseY)
	time.sleep(0.05)
	keyboard.press_and_release("alt+f4")
	# pyautogui.click(scrnW-20, 20, button='left')  # Move the mouse to XY coordinates and click it.
	pyautogui.click(scrnW//2, int(scrnH*0.52), button='left')

	return "🖥✅"
		# os.system("cls")

	# pyautogui.moveTo(scrnW, 0) # Move the mouse to XY coordinates.

	# pyautogui.click()          # Click the mouse.

def output_keyboard(text):
	keyboard.press_and_release("space")
	for i in text:
		if i == i.lower():
			keyboard.press_and_release(i)
		else:
			keyboard.press_and_release("shift+"+i)
		keyboard.press_and_release("space")
	return "🖥✅"

def screenshot():  
	filename = f"{time.time()}.jpg"
	pyautogui.screenshot(filename)
	return filename

def find_name(fig):
	lop=0
	dir=os.listdir("media/")
	for i in dir:
		if i[:3]==fig:
			lop+=1
	return fig+str(lop)
	
def ren(path, content):
	vb=find_name(content)
	if content=="vid":
		os.rename("media/"+path,"media/"+vb+".mp4")
	elif content=="pic":
		os.rename("media/"+path,"media/"+vb+".png")
	return vb
def video(vid):
	start_file(vid+".mp4")
	keyboard.press_and_release("F11")
	return "🖥✅"

def pict(pic):
	start_file(pic+".png")
	keyboard.press_and_release("F11")
	return "🖥✅"

def ip_address():
    try:
        ip = requests.get("http://jsonip.com/").json()
        response = requests.get(url=f'http://ip-api.com/json/{ip["ip"]}').json()
        # print(response)
        
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
        return pl
        
    except requests.exceptions.ConnectionError:
        return '[!] Please check your connection!'
        
def specifications():
	x,y=pyautogui.size()
	banner = f"""
	Name PC: {platform.node()}
	Processor: {platform.processor()}
	System: {platform.system()} {platform.release()}
	Screen size: {x}x{y}
	"""
	return banner

def raskladka():
	keyboard.press_and_release("shift+alt")
	return '🖥✅'

def cmdo(com):
	try:			res=subprocess.check_output(com, shell=1)
	except:			return '🖥❌'
	try:			res=res.decode('utf8')
	except:
		try:		res=res.decode('cp866')
		except:		return '🖥❌'
	return '🖥✅:\n'+res


def cmdi(com):
	try:
		os.system(com)
		return '🖥✅'
	except:
		return '🖥❌'


def commit(text):
	text="{"+text+"}"
	na4="0"
	kon="0"
	ret=[]
	for i in range(len(text)):
		if na4!="0" and kon!="0":
			ret.append(text[na4+1:kon])
			na4="0"
			kon="0"

		if text[i]=="{":
			na4=i
		if text[i]=="}":
			kon=i
	print(ret)
	return ret[0],ret[1]
def wget(text):
	link,save = commit(text)
	try:   		wg.download(link, "media/"+save);	return '🖥✅'
	except: 	return '🖥❌🗡'

def comm(text):
	comi4=re.findall(r'{([^<>]+)}', text)
	try:		return comi4, True
	except:		return None, False

def del_exit():
	dir=os.listdir("media/")
	for i in dir:
		os.remove("media/"+i)
	return "🖥✅"

def print_gui(text):
	try:		pyautogui.alert(text, "~");	return '🖥✅'
	except:		return '🖥❌'

def input_gui(text):
	try:		answer = pyautogui.prompt(text, "~")
	except:		return '🖥❌'
	return answer

def start_file(text):
	try:
		os.startfile("media\\"+text)
		return "🖥✅"
	except: return "🖥❌"

def com_bot(kl):
	res='❌Нет такой команды❌'#, зато есть такие:\n\nСписок функций и их использование:\n1. Выполнить команду, на её вывод всё-равно:    cmdi: <команда>\n2. Выполнить команду и вернуть её вывод в телеграмм: cmdo: <команда>\n3. Сохранить фото, аудио или видео на ПК:    просто отправить этот файл\n4. Скачать файл из интернета:    wget <ссылка>\n\nКоманты и ссылки обязателно надо писать в <>'
	try:
		inp,i=comm(kl)
		if kl.lower()[:4]=='cmdi' and i:
			res=cmdi(inp[0])

		elif kl.lower()[:4]=='cmdo' and i:
			res=cmdo(inp[0])

		elif kl.lower()[:4]=='wget' and i:
			res=wget(kl)

		elif kl.lower()[:4]=='pict' and i:
			res=pict(inp[0])

		elif kl.lower()[:4]=='vide' and i:
			res=video(inp[0])

		elif kl.lower()[:4]=='outp' and i:
			res=print_gui(inp[0])

		elif kl.lower()[:4]=='inpt' and i:
			res=input_gui(inp[0])

		elif kl.lower()[:4]=='strt' and i:
			res=start_file(inp[0])

		elif kl.lower()[:4]=='keyb' and i:
			res=output_keyboard(inp[0])

		elif kl.lower()[:4]=='scrn':
			res=screenshot()

		elif kl.lower()[:4]=='spec':
			res=specifications()

		elif kl.lower()[:4]=='rask':
			res=raskladka()

		elif kl.lower()[:4]=='ipad':
			res=ip_address()

		elif kl.lower()[:4]=='lock':
			res=lock()

		elif kl.lower()[:4]=='exit':
			res=del_exit()	

		return res


	except: return res
# print(ip_address())
# print(start_file(input()))
print(com_bot("pc3 wget {{https://i.ytimg.com/vi/1Z7L8FU9S2s/hqdefault.jpg} {lol.png}}"))