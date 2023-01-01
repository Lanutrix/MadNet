import telebot
import time

# a variable to store the timer and message counter for the specified chat
counter = None
chat_id = -607433374
bot = telebot.TeleBot("<token>")
flag = True


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    global counter, flag
    if 'запущен от имени' in message.text and flag:
        # start the timer and set the message counter to 1
        counter = {"counter": 1, "end_time": int(time.time()) + 60}
        bot.send_message(chat_id, 'all scrn')
        flag = False
    elif not flag:
        # increment the message counter
        counter["counter"] += 1


def check_timers():
    global counter
    # get the current time
    current_time = int(time.time())
    # if the timer has been started
    if counter is not None:
        # if the timer has expired
        if counter["end_time"] <= current_time:
            # send a message with the number of received messages
            bot.send_message(chat_id, f"Ботов онлайн: {counter['counter']}")
            # reset the timer and message counter
            counter = None


# run the check_timers function every second
while True:
    check_timers()
    time.sleep(1)
