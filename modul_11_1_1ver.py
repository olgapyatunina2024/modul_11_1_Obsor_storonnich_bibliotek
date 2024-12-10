import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from PIL import Image, ImageFilter


class Pillow:
    image = Image.open(r'C:\Users\PC\Desktop\Universitet\Python\Modul11\kat.jpg')
    resized_image = image.resize((800, 600))  # изменение размера 800 x 600
    resized_image.save(r'C:\Users\PC\Desktop\Universitet\Python\Modul11\kat_image.jpg')
    print('Изменение размера картинки')
    print()

    image = Image.open(r'C:\Users\PC\Desktop\Universitet\Python\Modul11\kat.jpg')
    blurred_image = image.filter(ImageFilter.BLUR)  # применить эффект
    blurred_image.save('kat_image1.jpg')
    print('Размытие картинки')
    print()

    image = Image.open(r'C:\Users\PC\Desktop\Universitet\Python\Modul11\kat.jpg')
    image.save('kat_image2.gif')  # конвертация в формат GIF
    print('Формат GIF')
    print()

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

#Данные о курсах валют
r = requests.get(URL)
json_flag = False
if r.ok:
    try:
        r = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Неформат json.', r, sep='\n')
    else:
        json_flag = True
pprint(r['Valute'])

print()

class Panda:
    # Данные из текстового файла
    data = pd.read_fwf(r'C:\Users\PC\Desktop\Universitet\Python\Modul11\readme.txt')
    print(data.head())

print()

class Numpy:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    sum = np.sum(arr)
    b = np.nonzero(arr < 5)
    flip = np.flip(arr)

    print('Массив')
    print(arr)
    print('Сумма элементов')
    print(sum)
    print('Элементы,меньшие 5')
    print(b)
    print('Массив в обратном порядке')
    print(flip)

print()

class Matplotlib:
    x = [-4,-3,-1,0, 1, 2, 3, 4]         # Данные по осям
    y = [16,9,1,0, 1, 4, 9, 16]
    print('Визуальные графики парабол нужно закрывать для корректноq работы кода')

    plt.plot(x, y)         # Парабола
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('График параболы')
    plt.show()
    plt.title('График параболы')
    plt.scatter(x, y, color='green')
    plt.show()
    print()

    print('Работа с библиотеками окончена')



