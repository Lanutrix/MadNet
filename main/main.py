import telebot
import config
import main.scr as scr
import main.pc as pc

bot=telebot.TeleBot(config.TOKEN_PC[pc.PPP][1])

@bot.message_handler(commands=['info'])
def start_message(message):
	bot.send_message(message.chat.id,"Список функций и их использование:\n1. Выполнить команду, на её вывод всё-равно: cmdi: <команда>\n2. Выполнить команду и вернуть её вывод в телеграмм: cmdo: <команда>\n3. Сохранить фото, аудио или видео на ПК: просто отправить этот файл\n4. Скачать файл из интернета: wget <ссылка>\n\nКоманты и ссылки обязателно надо писать в <>")	
	
	
@bot.message_handler(content_types=['text'])
def infokigb(message):
	gop=pc.pc_prov(message.text)
	if gop!=0:
		bot.send_message(message.chat.id,gop)

bot.polling(none_stop=True)