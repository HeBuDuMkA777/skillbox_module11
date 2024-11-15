print('Задача 5. Вот это объёмы!')

# Для курсовой работы по физике Андрею нужно сравнить объёмы двух планет: Земли
# и теоретически возможной для нашей Вселенной планеты. Андрей хорошо разбирается в формулах, но плохо считает.
# Объём Земли ему известен — это 1.08321 * 10 ** 12 км³.

# Объём теоретически возможной планеты ему нужно посчитать.
# У него есть формула: V = 4/3∙π∙R

# ‌В ней V — это объём, π — число пи, а R — радиус планеты.

# Что нужно сделать
# Напишите программу, которая получает на вход радиус случайной планеты и выводит на экран,
# во сколько раз планета Земля меньше или больше теоретически возможной планеты по объёму.
# Ответ округлите до трёх знаков после точки.

# Пример 1
# Введите радиус случайной планеты: 3389.5
# Объём планеты Земля больше в 6.641 раз

# Пример 2
# Введите радиус теоретически возможной планеты: 7000
# Объём планеты Земля меньше в (1/0.754) = 1.326 раз

import math 

volume_earth = 1.08321 * 10**12
radius_planet = float(input("Введите радиус теоретически возможной планеты: "))
volume_planet = (4 / 3) * math.pi * radius_planet ** 3

if volume_earth > volume_planet:
    result = round(volume_earth / volume_planet, 3)
    print("Объем планеты Земля больше в", result, "раз")
else:
    result = round(volume_planet / volume_earth, 3)
    print(f'Объем планеты Земля меньше в (1/{round(1 / result, 3)}) = {result} раз')