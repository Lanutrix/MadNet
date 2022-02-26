import main.scr as scr
import config
PPP=4
def pc_prov(pc):
	stroka=''
	try:
		for i in range(len(pc)):
			if pc[i]=='<':
				stroka+=pc[i:]
				break
			elif pc[i]!=' ':
				stroka+=pc[i]
				if pc[i].isdigit() and pc[i+1]==" ":
					l=stroka[:i+1]
					stroka+=' '
		for i in range(len(stroka)):
			if stroka[i]==' ' and stroka[i+1].isalpha():
				commj=stroka[i+1:]
				break
		print([l],[commj])
		if l==config.TOKEN_PC[PPP][0]:
			kop=scr.com_bot(commj)
			return kop
		else:
			return "🖥❌🗡"
	except: return 0#'Нет такой команды, зато есть такие:\n\nСписок функций и их использование:\n1. Выполнить команду, на её вывод всё-равно:    cmdi: <команда>\n2. Выполнить команду и вернуть её вывод в телеграмм: cmdo: <команда>\n3. Сохранить фото, аудио или видео на ПК:    просто отправить этот файл\n4. Скачать файл из интернета:    wget <ссылка>\n\nКоманты и ссылки обязателно надо писать в <>'
# print(pc_prov(input()))