import sys
import os
from . import KompasClass
#https://help.ascon.ru/KOMPAS_SDK/23/ru-RU/index.html

class Colection_process:
    """
    Класс колекций процедур для работы с компасом
    """
    def __init__(self):
        self.kompas = KompasClass.Kompas()

    def process1(self, file_path): 
        """
        Изменение Литер с сохранением 
        Выдаёт фукнцию которая сохраняет указанный фаил и его пдф в папку с изменением Лиетр
        аргумент - набор массивов ["первая литера", "вторая литера", "третья литера", "папка для сохранения"], [], ...
        если папка сохранениея пустая - сохраняеться в месте файла
        """
        def proc1(*args):
            for i, arg in enumerate(args, 1):
                try:    
                    #Открываем фаил 
                    self.kompas.open_document(file_path)

                    #Меняем литеры
                    self.kompas.set_litera_1(arg[0])
                    self.kompas.set_litera_2(arg[1])
                    self.kompas.set_litera_3(arg[2])

                    #Формируем адресс фаила сохранения 
                    if arg[3] != "" : 
                        folder_path = os.path.join(os.path.dirname(file_path), arg[3])
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        target_path = os.path.join(folder_path, os.path.basename(file_path))
                    else:
                        target_path = file_path

                    #Сохраняем фаил
                    self.kompas.save_document(target_path)

                    #Сохраняем фаил в пдф
                    pdf_path = os.path.splitext(target_path)[0] + ".pdf"
                    self.kompas.save_document(pdf_path)
                
                    #закрываем фаил без сохранения
                    self.kompas.close_document(False)

                except Exception as e:
                    print(f"Ошибка при открытии файла: {e}")
                    sys.exit(1)
        return proc1




    def process2(self, file_path: str): 
        """
        Сохранение спецификаций с новым стилем 
        :param file_path: полный путь к изменяемому файлу
        Функция выдаёт другую фукнцию для которой: 
        :param new_file: Имя папки в которую сохраняться новые спецификации, если пустой - сохраняться на старое место
        :param library_path: Полный путь до вашей библиотеки стилей
        :param style_id: номер применяемого стиля
        """
        def proc2(new_file: str, library_path: str, style_id: int=1):
            try:
                #Открываем фаил 
                self.kompas.open_document(file_path)

                #Меняем стиль надписи
                self.kompas.set_spec_library(library_path, style_id)

                #Формируем адресс фаила сохранения 
                if new_file != "" : 
                    folder_path = os.path.join(os.path.dirname(file_path), new_file)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    target_path = os.path.join(folder_path, os.path.basename(file_path))
                else:
                    target_path = file_path

                #Сохраняем фаил
                self.kompas.save_document(target_path)                

                #закрываем фаил без сохранения
                self.kompas.close_document(False)

            except Exception as e:
                print(f"Ошибка при открытии файла: {e}")
                sys.exit(1)
        return proc2
    



    def process3(self, file_path): 
        """
        Изменение Литер с сохранением в СПЕЦИФИКАЦИИ
        Выдаёт фукнцию которая сохраняет указанный фаил и его пдф в папку с изменением Лиетр
        аргумент - набор массивов ["первая литера", "вторая литера", "третья литера", "папка для сохранения"], [], ...
        если папка сохранениея пустая - сохраняеться в месте файла
        """
        def proc3(*args):
            for i, arg in enumerate(args, 1):
                try:    
                    #Открываем фаил 
                    self.kompas.open_document(file_path)

                    #Меняем литеры
                    self.kompas.fill_spec_stamp_multi({
                        40: arg[0],
                        41: arg[1],
                        42: arg[2],
                    })

                    #Формируем адресс фаила сохранения 
                    if arg[3] != "" : 
                        folder_path = os.path.join(os.path.dirname(file_path), arg[3])
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        target_path = os.path.join(folder_path, os.path.basename(file_path))
                    else:
                        target_path = file_path

                    #Сохраняем фаил
                    self.kompas.save_document(target_path)

                    #Сохраняем фаил в пдф
                    pdf_path = os.path.splitext(target_path)[0] + ".pdf"
                    self.kompas.save_document(pdf_path)
                
                    #закрываем фаил без сохранения
                    self.kompas.close_document(False)

                except Exception as e:
                    print(f"Ошибка при открытии файла: {e}")
                    sys.exit(1)
        return proc3









