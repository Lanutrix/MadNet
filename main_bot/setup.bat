@echo off
 
:: Ввод данных:
set /p Name="Name pc: "
set /p Token="Token: "

mkdir vers
mkdir media

:: "Идентификация" данных:
echo %Name% > token.txt
echo %Token% >> token.txt

echo "Installation completed"

pause>nul