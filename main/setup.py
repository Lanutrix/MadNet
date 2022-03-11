import os

ok=os.getcwd()

try:
    os.mkdir("vers")
    os.mkdir("media")
except:     pass

name = input("Введите имя компьютера: ")
token = input("Введите токен бота: ")

try:
    conf = open("token.txt", "w")
    conf.write(f"{name}\n{token}")
    alert = input("Всё установленно и готово к работе")
except:     i = input("Что-то пошло не так!!! ")