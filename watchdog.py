import subprocess
import time

# Имя процесса, который нужно следить
process_name = "process.exe"

while True:
    # Проверяем, запущен ли процесс
    try:
        output = subprocess.check_output(["tasklist"])
        if process_name not in output.decode("utf-8"):
            # Процесс не запущен, запускаем его
            subprocess.Popen([process_name])
    except:
        # Произошла ошибка при проверке или запуске процесса, игнорируем
        pass

    # Ждем некоторое время перед следующей проверкой
    time.sleep(60)
