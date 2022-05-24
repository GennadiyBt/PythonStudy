"""Задача 1. Напишите программу, которая принимает на вход вещественное 
число и показывает сумму его цифр(отсекаем минус, считаем все в плюс)."""

# num = input("Введите вещественное число: ")
# print(num)
# sum = 0
# for i in range(len(num)):
#     if num[i] != "-" and num[i] != "," and num[i] != ".":   # Учитываем вариант, когда пользователь в качестве
#                                                             # разделителя может использовать как "," так и "."
#         sum += int(num[i])
# print(sum)

"""Задача 2. Напишите программу, которая принимает 
на вход число N и выдает набор произведений чисел от 1 до N."""

# N = int(input("Введите целое число: "))
# result = []
# prom = 1
# for i in range(1, N+1):
#     prom *= i
#     result.append(prom)
# print(result)

"""Задача 3 Реализуйте случайное перемешивания списка."""

# Вариант 1

# def mix_list(list):
#     import random
#     random.shuffle(list)
#     return list
# list =  ['Веселый пианист', 250, 3.14, 'True ']
# print(mix_list(list))

# Вариант 2

# def mix_list2(list):
#     import random
#     list.sort(key = lambda x: random.random())
#     return list
# list =  ['Веселый пианист', 250, 3.14, 'True ']
# print(mix_list2(list))