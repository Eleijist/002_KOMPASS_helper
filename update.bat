@echo off
chcp 65001 >nul
setlocal

::здесь укажите путь к своему интропретатору
set "python_path=%cd%\venv\Scripts\python.exe"  

:: Определяем папки
set "root=%cd%\D_bag"
set "script_path=%cd%\algoritm.py"
set "temp_file=%temp%\file_list%random%.txt"


:: Создаем список всех файлов
echo Создаю список файлов...
(for /r "%root%" %%i in (*.cdw *.spw) do (
    echo %%~fi
)) > "%temp_file%"

:: Считаем количество файлов
set total=0
for /f "usebackq delims=" %%a in ("%temp_file%") do set /a total+=1
echo Найдено файлов: %total%
echo.


:: Читаем файл построчно и отправляем в Python
for /f "usebackq delims=" %%a in ("%temp_file%") do (
    echo Обрабатывается: %%~nxa
    "%python_path%" "%script_path%" "%%a"
)


del "%temp_file%" 2>nul
echo Готово! Обработано файлов: %processed%
pause