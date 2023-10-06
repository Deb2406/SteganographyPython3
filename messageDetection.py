import time
from stegano import lsb
from stegano import exifHeader
def decryptingPng(sicretPicture):
    try:
        print('Зашифрованное сообщение: '+lsb.reveal(sicretPicture)+'\n')
        time.sleep(1)
    except FileNotFoundError:
        print('Фаил не найден. Пожалуйста, убедитесь в правильности пути к файлу')
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


#Дешифрвоание jpg
def decryptingJpg(picture):
    try:
        print('Зашифрованное сообщение: '+exifHeader.reveal(picture).decode()+ '\n')
        time.sleep(1)
    except FileNotFoundError:
        print('Фаил не найден. Пожалуйста, убедитесь в правильности пути к файлу')
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")