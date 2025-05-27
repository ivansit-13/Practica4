#  Задание 1. Создайте массив размерностью 15. С помощью цикла for заполните массив
#  случайными числами. Выведите элементы массива используя цикл foreach;
#
# import random
#
# mymas = [0] * 15
#
# for i in range(15):
#     mymas[i] = random.randint(1, 100)
#
# for y in mymas:
#     print(y)

# Задание2.Создайте массив размерностью 15.Первые14 элементов пользователь вводит
# через консоль. В качестве последнего элемента записывается сумма всех элементов.
# Выведите элементы массива используя цикл foreach;
#
# mymas = [0] * 15
# counter = 0
#
# for i in range(14):
#     number = int(input(f"Введите {i+1} число массива - "))
#     mymas[i] = number
#     counter += number
#
# mymas[-1] = counter
#
# for y in mymas:
#     print(y)

# Задание 3. Напишите enum для математических операций (+,-, *, /). Создайте функцию,
# которая будет принимать 2 числа и операцию. Внутри функции создайте switch, который
# будет содержать case для каждой операции. Функция должна возвращать 4 значения
# (firstNumber, secondNumber, operation, result);
# Enum (перечисление) в Python — это набор фиксированных значений,
# каждое из которых имеет уникальное имя. Перечисления помогают организовать код,
# сделать его более читаемым и избежать ошибок,
# связанных с использованием «магических чисел» или строк.
# from enum import Enum
#
# # Задаем enum для математических операций
# class Operation(Enum):
#     ADD = '+'
#     SUB = '-'
#     MUL = '*'
#     DIV = '/'
#
# def meaning(first_number, second_number, operation):
#     match operation:
#         case Operation.ADD:
#             result = first_number + second_number
#         case Operation.SUB:
#             result = first_number - second_number
#         case Operation.MUL:
#             result = first_number * second_number
#         case Operation.DIV:
#             if second_number == 0:
#                 raise ValueError("делить на 0? ну что-то странное...")
#             result = first_number / second_number
#     return first_number, second_number, operation, result
#
#
# number1 = int(input("Введите 1 число - "))
# number2 = int(input("Введите 2 число - "))
# print("Что вы хотите делать с этими числами?")
# print("складывать - 1")
# print("вычитать - 2")
# print("умножать - 3")
# print("делить - 4")
# choice = int(input("Ваш выбор - "))
# if choice == 1:
#     operation = Operation.ADD
# elif choice == 2:
#     operation = Operation.SUB
# elif choice == 3:
#     operation = Operation.MUL
# elif choice == 4:
#     operation = Operation.DIV
# else:
#     print("вы указали что-то не то")
#
#
# try:
#     first_num, second_num, oper, res = meaning(number1, number2, operation)
#     print(f"{first_num} {oper.value} {second_num} = {res}")
# except ValueError as e:
#     print(e)

# Задание 4. Напишите функцию, которая будет преобразовывать введенную пользователем
# дату(за текущий год) к следующему виду;
# Input: 01.09.2021
# Output: Среда, 1 Сентября, 2021 год
# import datetime
#
# def transform_date(mydata):
#     days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
#     months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
#         'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
#     date = datetime.datetime.strptime(mydata, "%d.%m.%Y")
#     weekday = days[date.weekday()] #а тут дни недели начинаются с 0 - понедельник и воскресенье 6
#     day = date.day
#     month = months[date.month - 1] #мы вычитаем 1 так как в массиве у нас начинается всё с 0
#     year = date.year
#     return print(f"{weekday}, {day} {month}, {year} год")
#
# mydata = input("Введите дату по образцу (04.07.2007): ")
# transform_date(mydata)

# Задание 5. С помощью конструкции try..catch, обработайте участки кода в которых могут
# возникнуть исключения; (Задание 3)
# try:
#     a = int(input("Ведите число "))
#     print(a)
# except ValueError:
#     print("Вы ввели не число")
