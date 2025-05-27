# Задание 1. Посчитайте сумму целых чисел, расположенных между числами 1 и N
# включительно;
# number2 = int(input("Введите число до которого вы хотите вести счёт: "))
# counter = 0
# number1 = 1
# for i in range(number1,number2+1):
#     counter += i
# print(counter)

# Задание 2. Петя успевает по математике лучше всех в классе, поэтому учитель задал ему
# сложное домашнее задание, в котором нужно в заданном наборе целых чисел найти сумму
# всех положительных элементов, затем найти где в заданной последовательности
# находятся максимальный и минимальный элемент и вычислить произведение чисел,
# расположенных в этой последовательности между ними. Так же известно, что
# минимальный и максимальный элемент встречаются в заданном множестве чисел только
# один раз и не являются соседними. Напишите функцию, которая примет массив и вернет
# два числа (сумму положительных элементов и произведение чисел, расположенных между
# минимальным и максимальным элементами);
# def counter(mas):
#     number_sum = 0
#     for i in range(len(mas)):
#         if mas[i] > 0:
#             number_sum += mas[i]
#
#     min_value = min(mas)
#     max_value = max(mas)
#     min_index = mas.index(min_value)
#     max_index = mas.index(max_value)
#
#
#     start = min(min_index, max_index) + 1
#     end = max(min_index, max_index)
#
#     # Вычисляем произведение элементов между ними
#     multiplication = 1
#     for i in range(start, end):
#         multiplication *= mas[i]
#
#     return number_sum, multiplication
#
# mymas = [-1, 1, 2, 3, 4, 5]
# print(counter(mymas))


# Задание 3. Сформируйте возрастающий массив из случайных четных чисел;
# import random
#
# def mymas(len_mas,number1, number2):
#     mas = []
#     for i in range(len_mas):
#         mas.append(random.randint(number1,number2))
#     return mas
# print(mymas(7,1,999))

# Задание 4. Дана строка. Если она начинается на «abc», то замените их на «www», иначе
# добавьте в конец строки «zzz»;
# mystring = input("Введите свою строчку: ")
# if mystring[0:3] == "abc":
#     mystring = "www" + mystring[3:]
# else:
#     mystring = mystring + "zzz"
# print(mystring)

# Задание 5. Напишите функцию для вычисления значения выражения (a+4b)(a−3b)+a2;
# def counter(a,b):
#     counter = (a+4*b)*(a-3*b)+a*2
#     return counter
#
# a = int(input("Введите a - "))
# b = int(input("Введите b - "))
# print(counter(a, b))


# Задание 6. Дан массив, содержащий положительные и отрицательные числа. Замените
# все элементы массива на противоположные по знаку. Например, задан массив [1, -5, 0, 3,
# -4], после преобразования должно получиться [-1, 5, 0, -3, 4];
# mymas = [1, -5, 0, 3, -4]
# for i in range(len(mymas)):
#     if mymas[i] < 0:
#         mymas[i] = mymas[i] * -1
#     elif mymas[i] > 0:
#         mymas[i] = mymas[i] * -1
#     else:
#         continue
# print(mymas)

# Задание 7. Даны координаты точки и радиус круга с центром в начале координат.
# Определите, принадлежит ли данная точка кругу;
# r = 6
# x = 2
# y = 2
# if (x**2+y**2)**0.5 <= r:
#     print(True)
# else:
#     print(False)