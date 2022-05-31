# Задача 1. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def transform(num):
#     d = num
#     chact = num//2
#     ost = num%2 
#     result = []
#     while d >= 2:
#         result.append(ost)
#         d = chact
#         chact = d//2
#         ost = d%2
#     result.append(d)
#     result.reverse()
#     return result 

# n = int(input("Введите число, которое нужно преобразовать: "))
# print("".join(map(str, transform(n))))

# Задача 2. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# result = []
# def nega_fibonacci(n):
#     if n == -1:
#         return 1
#     if n == -2:
#         return -1
#     return nega_fibonacci(n+2) - nega_fibonacci(n+1)
        
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Введите число: "))
# for i in range(-n, 0):
#     result.append(nega_fibonacci(i))

# result.append(0)

# for i in range(1, n+1):
#     result.append(fibonacci(i))

# print(result)         # Рекурсия - это хорошо, но при больших значениях n (например 50) код зависает на 30+ минут

# Задача 3. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# def min_max(string):
#     dig_list = list(map(int,string.split()))
#     dig_list.sort()
#     print("Наибоьшее число равно ", dig_list[-1], "наименьшее число равно ", dig_list[0])

# digit_string = input("Введите числа, разделив их пробелами: ")

# min_max(digit_string)

# Задача 4. Задайте два целых числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# def least_com_mult(a, b):
#     if a > b:
#         max, min = a, b
#     else:
#         max, min = b, a
#     lcm = max
#     while lcm%min != 0:
#         lcm +=max
#     return lcm

# num1 = int(input("Введите первое число: ")) 
# num2 = int(input("Введите второе число: "))

# print("Наименьшее общее кратное чисел ", num1, " и ", num2, " равняется ", least_com_mult(num1, num2))

