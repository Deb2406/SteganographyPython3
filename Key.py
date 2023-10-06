import time
import os
from PIL import Image
from main import checkExtension

def encrypt_message(image_path, message, output_path, key):
    try:
        message=key+message
        # Open the image
        image = Image.open(image_path)
        width, height = image.size

        # Convert the message to binary
        binary_message = ''.join(format(ord(char), '08b') for char in message)

        # Ensure the message can fit in the image
        max_message_length = (width * height * 3) // 8
        if len(binary_message) > max_message_length:
            raise ValueError("Message is too long to fit in the image.")

        # Add a sentinel at the end of the binary message to mark the message's end
        binary_message += '1111111111111110'

        index = 0  # To keep track of the binary message index
        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y)))

                # Embed the message in the least significant bits of each color channel
                for color_channel in range(3):
                    if index < len(binary_message):
                        pixel[color_channel] = pixel[color_channel] & ~1 | int(binary_message[index])
                        index += 1

                # Update the pixel in the image
                image.putpixel((x, y), tuple(pixel))

        # Save the modified image with the encrypted message
        image.save(output_path)
        filePath = os.getcwd()
        print('\n' + f'Сообщение успешно зашифровано в {output_path}' + '\n'
                     f'Фаил находится в {filePath}' + '\n')
        time.sleep(1)

    except FileNotFoundError:
        print('Фаил не найден. Пожалуйста, убедитесь в правильности пути к файлу.')
    except Exception as e:
        print("Error:", str(e))

def decrypt_message(image_path, key):
    try:
    #Open the image
        image = Image.open(image_path)
        width, height = image.size

        binary_message = ''
        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y)))

                # Extract the least significant bit from each color channel
                for color_channel in range(3):
                    binary_message += str(pixel[color_channel] & 1)

        # Find the sentinel and extract the message
        sentinel_index = binary_message.find('1111111111111110')
        if sentinel_index == -1:
            raise ValueError("No message found in the image.")

        binary_message = binary_message[:sentinel_index]

        # Convert the binary message back to text
        message = ''
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i + 8]
            message += chr(int(byte, 2))

        sizeKey=len(key)
        if message[:sizeKey]==key:
            print("Зашифрованное сообщение:", message[sizeKey:])
        else:
            print("Пусто")

    except FileNotFoundError:
        print('Фаил не найден. Пожалуйста, убедитесь в правильности пути к файлу.')
    except Exception as e:
        print("Error:", str(e))

    # Example usage:
def userInputCript():
    print('На данный момент работает очень медленно, время шифровки до 2-х минут.'+'\n')
    time.sleep(1)

    startImage = input("Введите путь до изображения: ")
    secretImage = input('Введите название зашифрованного изображения: ')
    secretKey = input('Введите ключ (до 4 символов): ')
    secretMessage = input('Введите сообщение (поддерживает только англиский): ')

    startImage=checkExtension(startImage,'.png')
    secretImage=checkExtension(secretImage,'.png')
    start=time.time()
    encrypt_message(startImage, secretMessage, secretImage,secretKey[0:4])
    end=(time.time()-start)/60

    print('Время работы шифра {: 0.1f}'.format(end))

def userInputDecript():
    print('На данный момент работает очень медленно, время шифровки до 5-х минут.' + '\n')
    secretImage = input('Введите путь до изображения: ')
    secretKey = input('Введите ключ: ')

    secretImage = checkExtension(secretImage,'.png')

    start = time.time()
    decrypted_message = decrypt_message(secretImage, secretKey)
    end = (time.time() - start) / 60

    print('Время работы шифра {: 0.1f}'.format(end))

