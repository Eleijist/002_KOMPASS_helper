import sys
import os
#from KOMPAS_tools import Kompas
from libs.KompasClass import Kompas
from libs.Colection_process import Colection_process
#https://habr.com/ru/companies/ascon/articles/337288/
#https://pypi.org/project/KOMPAS-tools/


# 1. Проверяем, передан ли путь к файлу
if len(sys.argv) < 2:
    print("Ошибка: Укажите путь к файлу чертежа")
    print("Пример: python script.py C:\\МоиЧертежи\\Чертеж.cdw")
    sys.exit(1)

# 2. Подключаемся к Компасу
process = Colection_process()

# 3. Получаем путь к файлу из аргументов командной строки
file_path = sys.argv[1]



#process.process1(file_path)(["Э"," "," ","Литера Э"],[" "," "," ","Литера без"],["О"," "," ","Литера О"],["О","О1"," ","Литера О1"])
#process.process2(file_path)("", "D:\Пользователь\Документы пользователя\Компас\Мои стили\GRAPHIC.LYT")
#process.process4(file_path,{110:"Боярский", 111:"Лисицын", 113:"Щербаков", 114:"Сулацкая", 115:"Юрин", 10:"Т.контр."})(["Э"," "," ","Литера Э"],[" "," "," ","Литера без"],["О"," "," ","Литера О"],["О","О1"," ","Литера О1"])
process.process5(file_path)(["Э"," "," ","10.03.2024","Литера Э"],[" "," "," ","24.03.2024","Литера без"],["О"," "," ","04.06.2024","Литера О"],["О","О1"," ","27.12.2024","Литера О1"])
#process.process6(file_path)(["Э"," "," ","10.03.2024","Литера Э"],[" "," "," ","24.03.2024","Литера без"],["О"," "," ","04.06.2024","Литера О"],["О","О1"," ","27.12.2024","Литера О1"])

# основной процесс переберает все свои аргументы записывает их в фаил и обрабатывает
#for path in sys.argv[1:]:
#    if os.path.exists(path):
#        print(f"Обработка файла: {path}")
#        file_path = path
#        process(["Э"," "," ","Литера Э"],[" "," "," ",""],["О"," "," ","Литера О"],["О","О1"," ","Литера О1"])
#    else:
#        print(f"Файл не найден: {path}")