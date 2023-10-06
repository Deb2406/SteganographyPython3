from stegano import lsb,exifHeader
import os
import time



#Шифрование в png
def encryptionPng(picture,sicretPicture,userMessage):
    try:
        #Прячем сообщения в байтх
        secret = lsb.hide(picture, userMessage)
        #Сохранения изображения в файлах
        secret.save(sicretPicture)
        #Путь где лежит сохраненный файл
        filePath = os.getcwd()
        print('\n'+f'Сообщение успешно зашифровано в {sicretPicture}' + '\n'
              f'Фаил находится в {filePath}'+'\n')
        time.sleep(1)
    except FileNotFoundError:
        print('Фаил не найден. Пожалуйста, убедитесь в правильности пути к файлу.')
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')


#Шифрование jpg
def encryptionJpg(picture,sicretPicture,userMessage):
    try:
        secret = exifHeader.hide(picture, sicretPicture, userMessage)

        filePath = os.getcwd()
        print(f'Сообщение успешно зашифровано в {sicretPicture}' + '\n'
              f'Фаил находится в {filePath}')
    except FileNotFoundError:
        print('Фаил не найден. Пожалуйста, убедитесь в правильности пути к файлу')
    except Exception as e:
        print(f'Произоша ошибка: {str(e)}')

