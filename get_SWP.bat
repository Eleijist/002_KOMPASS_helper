@echo off
chcp 65001 >nul
setlocal

:: Определяем папки
set "root=%cd%"
set "hom=%root%\D_SWP"

:: Создаем папку, если её нет
if not exist "%hom%" mkdir "%hom%"

echo Перемещаем SWP файлы в %hom%...

:: Ищем и перемещаем файлы
for /r "%root%" %%i in (*.spw) do (
    echo "%%~dpni" | findstr /i /c:"%hom%" >nul || (
        echo   Перемещается: %%~nxi
        move "%%i" "%hom%" >nul
    )
)

echo Готово!
pause