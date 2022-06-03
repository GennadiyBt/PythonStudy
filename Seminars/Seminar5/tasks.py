# def ascen_seq(list_arg):
#     result_list = []
#     temp = list_arg[0]
#     for i in range(len(list_arg)-1):
#         result_list1 = []
#         if temp > list_arg[i]:
#             temp = list_arg[i]
#         result_list1.append(temp)
#         k = 0
#         for j in range(i, len(list_arg)-1):
#             if result_list1[k] < list_arg[j+1] and list_arg[j+1] < max(list_arg[(j+1):]):
#                 result_list1.append(list_arg[j+1])
#                 k +=1            
#         if   list_arg[-1] >  result_list1[-1]:
#             result_list1.append(list_arg[-1])
#         if len(result_list) < len(result_list1):
#             result_list = result_list1
#         temp = result_list1[0]
#     return result_list



# print(ascen_seq([2,1,5,9,4,5,2,3,6,7,12,1,2,3,10,11]))

# Написать программу вычисления арифметического выражения заданного строкой.
#  Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5

# def calc(arifm_str):
#     arifm_list_temp = [i for i in arifm_str]
#     arifm_list_temp.append('')
#     data = {'+','-','/','*',''}
#     arifm_list = []
#     temp_str = ''
#     for i in range(len(arifm_list_temp)):
#         if arifm_list_temp[i] not in data:
#             temp_str += arifm_list_temp[i]
#         else:
#             arifm_list.append(temp_str)
#             arifm_list.append(arifm_list_temp[i])
#             temp_str = ''
#     arifm_list.pop()
#     for i in range(len(arifm_list)):
#         if arifm_list[i]not in data:
#             arifm_list[i] = int(arifm_list[i])
#     for i in range(1, len(arifm_list)-1):
#         if arifm_list[i-1] == '-':
#             arifm_list[i] = -1*arifm_list[i]
#             arifm_list[i-1] = '+'
#     prom_result_list = []
#     i = 0
#     while i < len(arifm_list)-1:
#         if arifm_list[i+1] == '/':
#             prom_result_list.append(arifm_list[i]/arifm_list[i+2])
#             i +=3
#         elif arifm_list[i+1] == '*':
#             prom_result_list.append(arifm_list[i]*arifm_list[i+2])
#             i +=3
#         else:
#             prom_result_list.append(arifm_list[i])
#             i +=1
#     result = prom_result_list[0]
#     for i in range(1, len(prom_result_list)-1):
#         if prom_result_list[i] == '+':
#             result += prom_result_list[i+1]
#     return result
            
# test_str = '22+16/2-4*13'
# print(calc(test_str))