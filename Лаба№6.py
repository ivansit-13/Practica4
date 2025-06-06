# Задание 1. Создайте список с 10-ю именами. Выведите из этого списка имена начинающиеся
# на А;
# mas_name = ['Артём','Кеша','Андрей','Олег','Ксюша','Кира','Степан','Антон','Александр','Михаил']
# for i in range(len(mas_name)):
#     name = mas_name[i]
#     if name[0] == "А":
#         print(name)
from dataclasses import dataclass
from symtable import Class

# Задание 2. Создайте класс User с свойствами Login и Password. Создайте список объектов
# User из 5 элементов. Выведите из этого списка пользователя с определенными логином и
# паролем;

# class User:
#     def __init__(self,login,password):
#         self.login = login
#         self.password = password
#
# user_list = [User('MIKE',111),User('Kiko',123),
#              User('Stepan', 999),User('miko',987)
#             ,User('gigo',564)]
#
# name = 'MIKE'
# for user in user_list:
#     if user.login == name:
#         print(user.login,user.password)

# Задание 3. Создайте класс Task описывающий занятие, с свойствами: DateStart, DateFinish,
# Description. Создайте список объектов Task из 5 элементов. Выведите информацию о занятии
# заканчивающемся позже всех;
# import datetime
#
# class Task:
#     def __init__(self,DateStart,DateFinish,Description):
#         self.DateStart = DateStart
#         self.DateFinish = DateFinish
#         self.Description = Description
# task_list = [Task('04-12-2007','08-12-2007','Игорь'),
#              Task('08-12-2018','08-12-2019','Игорь'),
#              Task('12-08-1945','12-09-1945','Игорь'),
#              Task('20-07-2023','20-08-2023','Игорь'),
#              Task('13-12-2022','13-01-2023','Игорь')]
# data_min = datetime.datetime.strptime(task_list[0].DateFinish,'%d-%m-%Y')
# mas = []
# for task in task_list:
#     data = datetime.datetime.strptime(task.DateFinish,'%d-%m-%Y')
#     if data < data_min:
#         data_min = data
#         mas = [task.DateStart,task.DateFinish,task.Description]
# print(mas)


# Задание 4. Дана целочисленная последовательность, содержащая как положительные, так
# и отрицательные числа. Вывести ее первый положительный элемент и последний
# отрицательный элемент;
#
# mas_number = [1,2,3,4,5,6,-1,-8,-3]
# mas_M = []
# mas_P = []
# for i in range(len(mas_number)):
#     if mas_number[i] < 0:
#         mas_M.append(mas_number[i])
#     else:
#         mas_P.append(mas_number[i])
# print(mas_P[0],mas_M[-1])

# Задание 5. Дан символ С и строковая последовательность А. Найти количество элементов
# А, которые содержат более одного символа и при этом начинаются и оканчиваются символом
# С;
#
# C = "а"
# A = ['ананаса','пирог','дениал','a']
# counter = 0
# for i in range(len(A)):
#     name = A[i]
#     if len(name) > 1 and name[0] == C and name[-1] == C:
#         counter += 1
# print(counter)