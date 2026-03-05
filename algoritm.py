import sys
import os
#from KOMPAS_tools import Kompas
from libs.KompasClass import Kompas
#https://habr.com/ru/companies/ascon/articles/337288/
#https://pypi.org/project/KOMPAS-tools/


# 1. Проверяем, передан ли путь к файлу
if len(sys.argv) < 2:
    print("Ошибка: Укажите путь к файлу чертежа")
    print("Пример: python script.py C:\\МоиЧертежи\\Чертеж.cdw")
    sys.exit(1)

# 2. Подключаемся к Компасу
kompas = Kompas()
print(kompas.info_general())


# 3. Получаем путь к файлу из аргументов командной строки
file_path = sys.argv[1]






def process(*args):
    for i, arg in enumerate(args, 1):
        try:    
            #Открываем фаил 
            kompas.open_document(file_path)

            #Открываем фаил 
            kompas.open_document(file_path)

            #Меняем литеры
            kompas.set_litera_1(arg[0])
            kompas.set_litera_2(arg[1])
            kompas.set_litera_3(arg[2])

            #Формируем адресс фаила сохранения 
            if arg[3] != "" : 
                folder_path = os.path.join(os.path.dirname(file_path), arg[3])
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                target_path = os.path.join(folder_path, os.path.basename(file_path))
            else:
                target_path = file_path

            #Сохраняем фаил
            kompas.save_document(target_path)

            #Сохраняем фаил в пдф
            pdf_path = os.path.splitext(target_path)[0] + ".pdf"
            kompas.save_document(pdf_path)

            #закрываем фаил без сохранения
            kompas.close_document(False)

        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")
            sys.exit(1)



process(["Э"," "," ","Литера Э"],[" "," "," ","Литера без"],["О"," "," ","Литера О"],["О","О1"," ","Литера О1"])

# основной процесс переберает все свои аргументы записывает их в фаил и обрабатывает
#for path in sys.argv[1:]:
#    if os.path.exists(path):
#        print(f"Обработка файла: {path}")
#        file_path = path
#        process(["Э"," "," ","Литера Э"],[" "," "," ",""],["О"," "," ","Литера О"],["О","О1"," ","Литера О1"])
#    else:
#        print(f"Файл не найден: {path}")