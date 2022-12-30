import asyncio
import subprocess
import ctypes

process_name = "example.exe"  # имя процесса, который нужно проверить
process_file_path = "C:\\Path\\To\\Process\\File\\example.exe"  # путь к файлу процесса

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

        await asyncio.sleep(60)  # ждем 60 секунд перед следующей проверкой

asyncio.run(check_and_restart_process())
