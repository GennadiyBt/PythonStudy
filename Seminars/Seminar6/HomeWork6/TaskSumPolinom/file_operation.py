def file_write(file_name, polinom_str):    
    with open(file_name, 'w') as data:
        data.write(polinom_str)


def file_read(file_name):
    data = open(file_name, 'r')
    for line in data:
        polinom = line
    data.close
    return polinom

import generation_polinom as gen
test_list1 = [-5, -2, 3, 0, 2, 3]
test_list2 = [1, -2, 0, 1, 0, 3]

file_write('testpol1.txt', gen.polinom(test_list1))
file_write('testpol2.txt', gen.polinom(test_list2))

