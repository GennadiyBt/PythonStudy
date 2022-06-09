# Функция формирует полином по заданному списку коэффициентов. 
# Количество заданных коэффициентов определяет высшую степень многочлена.
def polinom(list_arg):
    k = len(list_arg) - 1
    result_list = []
    for i in range(k-1):
        if list_arg[i] != 0 and list_arg[i] != 1:
            result_list.append(str(list_arg[i])+'*x^'+str(k-i))   
        elif list_arg[i] != 0:
            result_list.append('x^'+str(k-i))
    if list_arg[k-1] != 0:
        result_list.append(str(list_arg[k-1])+'*x')
    if list_arg[k] != 0:
        result_list.append(str(list_arg[k]))
    result = result_list[0]
    for i in range(1, len(result_list)):
        if result_list[i][0] != '-':
            result += '+'+ result_list[i]
        else:
            result += '-'+ result_list[i][1:]
    result += '=0'
    
    return result

