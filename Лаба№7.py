# Задание 1. Дана строковая последовательность. Найти сумму длин всех строк, входящих в
# данную последовательность;
# mas = ['Максим','Апотекарий', 'Мерос', 'Алибаба']
# counter = 0
# for i in range(len(mas)):
#     counter += len(mas[i])
# print(counter)
from symtable import Class

# Задание 2. Дана целочисленная последовательность. Извлечь из нее все положительные
# числа;
# mas = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4]
# new_mas = []
# for i in range(len(mas)):
#     if mas[i] > 0:
#         new_mas.append(mas[i])
# print(new_mas)

# Задание 3. Дана целочисленная последовательность. Извлечь из нее все положительные
# двузначные числа, отсортировав их по возрастанию;
# mas = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,13,12,0]
# new_mas = []
# for i in range(len(mas)):
#
#     if len(str(mas[i])) > 1 and mas[i] > 0:
#         new_mas.append(mas[i])
# print(new_mas)

# Задание 4. Создать класс описывающий фитнес-центр с свойствами: Код клиента, Год,
# Номер месяца, Продолжительность занятия. Создайте список объектов класса фитнес-центр
# из 5 элементов. Вывести информацию о самом продолжительном и самом коротком занятиях;
# class my_fit:
#     def __init__(self,code_k,years,number_m,time_work):
#         self.code_k = code_k
#         self.years = years
#         self.number_m = number_m
#         self.time_work = time_work
#
# user_my_fit = [
#     my_fit(1,2007,5,56),
#     my_fit(2,2005,3,245),
#     my_fit(3,2003,2,24),
#     my_fit(4,2002,3,53),
#     my_fit(5,2009,2,36)
# ]
# max_time = 0
# min_time = 9999
# for My_fit in user_my_fit:
#     if My_fit.time_work > max_time:
#         max_time = My_fit.time_work
#     elif My_fit.time_work < min_time:
#         min_time = My_fit.time_work
# print("Максимальное время ",max_time)
# print("Минимальное время ",min_time)


# Задание 5. Создать класс описывающий фитнес-центр с свойствами: Код клиента, Год,
# Номер месяца, Продолжительность занятия. Создайте список объектов класса фитнес-центр
# из 10 элементов. Определить год, в котором суммарная продолжительность занятий всех
# клиентов была наибольшей, и вывести этот год и наибольшую суммарную
# продолжительность. Если таких годов было несколько, то вывести наименьший из них;
# class my_fit:
#     def __init__(self,code_k,years,number_m,time_work):
#         self.code_k = code_k
#         self.years = years
#         self.number_m = number_m
#         self.time_work = time_work
#
# user_my_fit = [
#     my_fit(1,2007,5,56),
#     my_fit(2,2005,3,245),
#     my_fit(3,2003,2,24),
#     my_fit(4,2002,3,53),
#     my_fit(4,2007,3,53),
#     my_fit(4,2005,3,53),
#     my_fit(4,2005,3,53),
#     my_fit(4,2009,3,53),
#     my_fit(4,2002,3,53),
#     my_fit(5,2009,2,36)
# ]
#
# year_sums = {}
# for i in user_my_fit:
#     year = i.years
#     my_time_work = i.time_work
#     if year in year_sums:
#         year_sums[year] += my_time_work
#     else:
#         year_sums[year] = my_time_work
#
# max_time_work = max(year_sums.values())
# years_with_max = []
# for year, my_time_work in year_sums.items():
#     if my_time_work == max_time_work:
#         years_with_max.append(year)
# year = min(years_with_max)
#
# print("Год с наибольшей суммарной продолжительностью занятий ", year)
# print("Наибольшая суммарная продолжительность = ",max_time_work)