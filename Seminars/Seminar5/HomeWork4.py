# Задача 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# def random_coef(k):
#     from random import randint
#     random_coef_list = [randint(0,101) for i in range(k+1)]
#     return random_coef_list


# def polinom(list_arg):
#     k = len(list_arg) - 1
#     result_list = [str(list_arg[i])+'*x**'+str(k-i) for i in range(k-1) if list_arg[i] != 0]
#     if list_arg[k-1] != 0:
#         result_list.append(str(list_arg[k-1])+'*x')
#     if list_arg[k] != 0:
#         result_list.append(str(list_arg[k])) 
#     result = ' + '.join(result_list) + ' = 0'
#     return result


# k = int(input("Введите показатель степени многочлена: "))
# with open('polinom.txt', 'w') as data:
#     data.write(polinom(random_coef(k)))



# Задача 35. В файле находится N натуральных чисел, 
# записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# def list_in_file(file_name):
#     data = open(file_name, 'r')
#     list_file = []
#     for line in data:
#         list_on_str = list(map(int, line.split()))
#         list_file = list_file + list_on_str #Данная строка нужна для случая, когда данные в файле записаны в несколько строк.
#     print(list_file)
#     return list_file
#     data.close


# # Задача решается исходя из посыла, что отсутствующий элемент не является первым или последним. 
# # В противном случае будет вариативность результата, ибо искомый элемент сможет находиться как на первом, так и на последнем месте. 
# def find_num(list_arg):
#     base = list_arg[0]
#     for i in range(len(list_arg)):
#         if list_arg[i] != base:
#             return base
#         base +=1



# Задача 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# def uni_elem(list_arg):
#   return [i for i in list_arg if list_arg.count(i)==1]


# start_list = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]

# print(uni_elem(start_list))