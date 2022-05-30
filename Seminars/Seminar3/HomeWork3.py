# Задача 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# def summ_odd_elements(list):
#     sum = 0
#     if len(list) < 2:
#         print("Сумма элементов на нечетных позициях равна ", sum)
#     else:
#         for i in range(1, len(list), 2):
#             sum += list[i]
#         print("Сумма элементов на нечетных позициях равна ", sum)

# list = [2, 3, 5, 9, 3, 4]
# summ_odd_elements(list)

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

# def product_pair(list):
#     if len(list)%2 == 0:
#         num = len(list)//2
#     else:
#         num = len(list)//2 + 1
#     list_result = []
#     for i in range(num):
#         list_result.append(list[i]*list[len(list)-1-i])
#     print(list_result)
# list = [2, 3, 5, 6]
# product_pair(list)

# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Вариант 1.
# def diff_min_max(list):
#     for i in range(len(list)):
#         list[i] = list[i] - int(list[i])
#     list.sort()    
#     while list[0] == 0:
#         list.remove(0)
#     result = list[-1] - list[0]
#     return result

# Вариант 2.
# def diff_min_max(list):
#     for i in range(len(list)):
#         list[i] = list[i]%1
#     list.sort()    
#     while list[0] == 0:
#         list.remove(0)
#     result = list[-1] - list[0]
#     return result


# test_list = [1.1, 1.2, 3.1, 5, 6, 7, 10.01]
# print(diff_min_max(test_list))
