from hideMessage import encryptionPng, encryptionJpg
from messageDetection import decryptingPng,decryptingJpg
from helpMenu import menuHelp

import re
import Key
import time

def message():
    print('Приветсвую в стеганографическом скрипте.')
    print('@author Deb' + '\n' + '@version 0.5' + '\n')

def check(text):
    return bool(re.search('[\u0400-\u04FF]', text))

# проверка на наличие png
def checkExtension(fileName,extension):
    if not fileName.endswith(extension):
        return fileName + extension
    else:
        return fileName
#Функция предоставляющая пользователю выбор, шифровки
def userChose():
    print('Выберете подходящий режим.')
    while True:
            user = int(input(
                "1.Шифровка сообщения в изображении (формат png)" + '\n'
                "2.Дешифровка сообщения из изображения (формат png)" + '\n' + '\n'
                "3.Шифровка сообщения в изображении (формат jpg)" + '\n'
                "4.Дешифровка сообщения из изображения (формат jpg)" + '\n' + '\n'
                "5.Шифровка сообщения в изображении с использованием ключа (формат png)" + '\n'
                "6.Дешифровка сообщения из изображения с использованием ключа (формат png)" + '\n' + '\n'
                "7.Меню помощи" + '\n'
                "8.Выйти из программы" + '\n'
                "Ваш выбор: "))
            if user == 1:
                picture = (input('\n' + "Введите полный путь до изображения: "))
                sicretPicture = (input("Введите какое название вы хотите у зашифрованного изображения: "))
                userMessage = (input(
                    "Введите сообщение которое хотите зашифровать (пока не поддреживает русский язык, в разработке): "))
                while True:
                    if not check(userMessage):
                        break
                    else:
                        print('В вашем сообщении находится кириллица.'+'\n'+
                              'При дешифровке,возможно некорректный вывод.'+'\n')
                        loop=input('Продолжить д/н:')
                        if loop=='д':
                            break
                #Проверка на расширение файл
                picture=checkExtension(picture,'.png')
                sicretPicture=checkExtension(sicretPicture,'.png')
                #Шифровка сообщения в изображении
                encryptionPng(picture,sicretPicture,userMessage)

            elif user == 2:
                # Проверка на расширение файл
                sicretPicture = (input('\n' + "Введите полный путь до изображения: "))
                # Дешифровка сообщения из изображения
                sicretPicture=checkExtension(sicretPicture,'.png')

                decryptingPng(sicretPicture)

            elif user == 3:
                picture = (input('\n' + "Введите полный путь до изображения: "))
                sicretPicture = (input("Введите какое название вы хотите у зашифрованного изображения: "))
                userMessage = (input("Введите сообщение которое хотите зашифровать: "))

                # Проверка на расширение файл
                picture = checkExtension(picture, '.jpg')
                sicretPicture = checkExtension(sicretPicture, '.jpg')

                # Шифровка сообщения в изображении
                encryptionJpg(picture,sicretPicture,userMessage)

            elif user==4:
                sicretPicture = (input('\n' + "Введите полный путь до изображения: "))
                # Проверка на расширение файл
                sicretPicture = checkExtension(sicretPicture, '.jpg')
                decryptingJpg(sicretPicture)
            elif user == 5:
                Key.userInputCript()
            elif user==6:
                Key.userInputDecript()
            elif user == 7:
                #вызов меню помощи из другого файла
                menuHelp()
            elif user==8:
                print('Выход из программы')
                time.sleep(1)
                break
            else:
                print('Incorrect')

def main():
    message()
    userChose()

if __name__ == '__main__':
    main()