import os


def spacefiller(path):
    spacefiller_command = f"fsutil file createnew {path}"
    os.system(spacefiller_command)


spacefiller(input("Введите полный путь (включая файл и его расширение, a также размер файла в байтах):  "))
print("Успех")
# Пример: C:\Users\Romeo558\Desktop\file.txt 102410
