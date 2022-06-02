def list_in_file(file_name):
    data = open(file_name, 'r')
    list_file = []
    for line in data:
        list_on_str = list(map(int, line.split()))
        list_file = list_file + list_on_str #Данная строка нужна для случая, когда данные в файле записаны в несколько строк.
    print(list_file)
    return list_file
    data.close


# Задача решается исходя из посыла, что отсутствующий элемент не является первым или последним. 
# В противном случае будет вариативность результата, ибо искомый элемент сможет находиться как на первом, так и на последнем месте. 
def find_num(list_arg):
    temp_step = list_arg[0]
    prom_list = [i for i in range(len(list_arg)+1)]
    temp_list = list(map(lambda x: x+temp_step, prom_list ))
    eps_num_list = [x for x in temp_list if x not in list_arg]
    eps_num = eps_num_list[0]
    
    return eps_num

print(find_num(list_in_file('data.txt')))