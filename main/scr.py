import subprocess, os
import re
import wget as wg

opa_pc=0
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
	cmdi("start media/"+vid+".mp4")
def pict(pic):
	cmdi("start media/"+pic+".png")
# print(ren("f","pic"))
def cmdo(com):
	try:
		res=subprocess.check_output(com, shell=1)
	except:
		return '🖥❌'
	try:
		res=res.decode('utf8')
	except:
		try:
			res=res.decode('cp866')
		except:
			return '🖥❌'
	return '🖥✅:\n'+res


def cmdi(com):
	try:
		os.system(com)
		return '🖥✅'
	except:
		return '🖥❌'

def wget(link,save):
	try:
		wg.download(link, "media/"+save)
		return '🖥✅'
	except: return '🖥❌🗡'
def comm(text):
	comi4=re.findall(r'<([^<>]+)>', text)
	try:
		return comi4, True
	except:
		return None, False

def del_exit(lpli):
	dir=os.listdir("media/")
	for i in dir:
		os.remove("media/"+i)
	return "kill"

def com_bot(kl):
	res='Нет такой команды'#, зато есть такие:\n\nСписок функций и их использование:\n1. Выполнить команду, на её вывод всё-равно:    cmdi: <команда>\n2. Выполнить команду и вернуть её вывод в телеграмм: cmdo: <команда>\n3. Сохранить фото, аудио или видео на ПК:    просто отправить этот файл\n4. Скачать файл из интернета:    wget <ссылка>\n\nКоманты и ссылки обязателно надо писать в <>'
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
		elif kl.lower()[:4]=='exit' and i:
			res=del_exit(inp[0])
		return res


	except: return res
# print(del_exit("kkd"))
# print(cmdo("dir"))