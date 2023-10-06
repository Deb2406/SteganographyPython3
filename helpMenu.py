def menuHelp():
    print('Что такое стегонография? Каким образом скрипт шифрует сообщение? ' + '\n' +
          '[+] Стеганогра́фия — способ передачи или хранения информации с учётом сохранения в тайне самого факта такой передачи.' + '\n' +
          '[+] Этот скрипт шифрует данные (в нашем случае сообщение) в изображении, путем изменения определенных пикселей. '
          'Дешифрует чтением этих пикселей.' + '\n' + '\n'
                                                      
          'Возможные проблемы и пути их решения:' + '\n'
          '1.В случае передачи изображения для дешефровки и скрипт резко виснет, '
          'возможно в изображении отстутсвует сообщение (пытаюсь выяснить причин)' + '\n' +

          '2.Возможная ошика что в пути вы забыли указать САМ документ например:'
          '(C:\\weLive\\weLove\\weLie\\название_вашего_документа.docx' + '\n' +

          '3.Для того что бы не писать каждый раз полный путь до изображения'
          ',можно создать отдельную папку со скриптом,куда можно положить изображение ' + '\n' +

          '4.Передал сообщение изображение через популярный мессенджер или соц.сеть и при попытке дешифровать выдает ошибку.' + '\n' +
          'Популярные мессенджеры и соц.сети убирают все "битые пиксели", так что нужно передовать через архив (RAR or 7Zip)' + '\n'
                                                                                                                                
          '5.В остальных случаях можете писать мне в тг' + '\n')

    while True:
        user = input('Выйти в главное меню д/н: ')
        if user == 'д':
            return