import scr
import pc
import telebot
import config
import sys

bot=telebot.TeleBot(config.TOKEN_PC[pc.PPP][1])

@bot.message_handler(commands=['info'])
def start_message(message):
	bot.send_message(message.chat.id,"Список функций и их использование:\n1. Выполнить команду, на её вывод всё-равно: cmdi: <команда>\n2. Выполнить команду и вернуть её вывод в телеграмм: cmdo: <команда>\n3. Сохранить фото, аудио или видео на ПК: просто отправить этот файл\n4. Скачать файл из интернета: wget <ссылка>\n\nКоманты и ссылки обязателно надо писать в <>")	
	
	
@bot.message_handler(content_types=['text'])
def infokigb(message):
    gop=pc.pc_prov(message.text)
    if gop!=0 and gop!="kill":
        bot.send_message(message.chat.id,gop)
@bot.message_handler(content_types=['photo'])
def handle_docs_document(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'media/' + message.photo[1].file_id 
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    picu=scr.ren(message.photo[1].file_id, "pic")
    print(str(message.chat.id))
    bot.reply_to(message, f"OK. Сохранил как {picu}\n")

@bot.message_handler(content_types=['video'])
def get_file(message):
    file_name = 'media/' + message.json['video']['file_name']
    file_info = bot.get_file(message.video.file_id)
    with open(file_name, "wb") as f:
        file_content = bot.download_file(file_info.file_path)
        f.write(file_content)
    video=scr.ren(file_name[5:],"vid")
    bot.reply_to(message, f"OK. Сохранил как {video}")


@bot.message_handler(content_types=['document'])
def handle_file(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'media/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "🖥✅")
    except Exception as e:
        bot.reply_to(message, f"🖥❌\n{e}")

def screen(img):
    with open("media/"+img, "rb") as file:
        bot.send_photo()


bot.polling(none_stop=True)