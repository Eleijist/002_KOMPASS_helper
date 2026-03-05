@echo off
chcp 65001 >nul
setlocal

:: Определяем папки
set "root=%cd%"
set "hom=%root%\bag ⊗"

:: Создаем папку, если её нет
if not exist "%hom%" mkdir "%hom%"

echo Копируем CPW и SWP файлы в %hom%...

:: Ищем и перемещаем файлы
for /r "%root%" %%i in (*.cdw *.spw) do (
    echo "%%~dpni" | findstr /i /c:"%hom%" >nul || (
        echo   Копируеться: %%~nxi
	    copy "%%i" "%hom%" >nul
    )
)

echo Готово!
pause