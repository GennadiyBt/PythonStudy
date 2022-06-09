def convert_in_list(polinom_string):
    polinom_string = polinom_string[:-2]
    polinom_list = polinom_string.split('+')
    return polinom_list


def negative_out(polinom_string):
    resalt_string = ''
    for i in range (1,len(polinom_string)-1):
        if polinom_string[i] == '-':
            resalt_string = polinom_string[:i]+'+'+polinom_string[i:]
    return resalt_string


def list_in_dict(list_arg):
    temp_list = []
    for item in list_arg:
        if item[0] == 'x':
            item = '1*'+ item
        if item[-1] == 'x':
            item = item + '^1'
        temp_list.append(item.split('*'))
    if not('x' in temp_list[-1]):
        temp_list[-1].append('x^0')
    for i in range(len(temp_list)):
        temp_list[i][0] = int(temp_list[i][0])
        temp_list[i].reverse()
    dikt_polinom = dict(temp_list)
    return dikt_polinom


def uniq_keys(dikt1, dikt2):
    list_keys = list(dikt1.keys())+list(dikt2.keys())
    list_uniq_keys = sorted(list(set(list_keys)))
    list_uniq_keys.sort(reverse = True)
    return list_uniq_keys


def sum_polinoms(test_polinom1, test_polinom2):
    list_polinom1 = convert_in_list(negative_out(test_polinom1))
    list_polinom2 = convert_in_list(negative_out(test_polinom2))
    dikt_pol1 = list_in_dict(list_polinom1)
    dikt_pol2 = list_in_dict(list_polinom2)

    list_uniq_keys = uniq_keys(dikt_pol1, dikt_pol2)
    result_list =[]
    for i in range(len(list_uniq_keys)):
        temp_list =[]
        coef = dikt_pol1.get(list_uniq_keys[i],0)+dikt_pol2.get(list_uniq_keys[i],0)
        temp_list.append(coef)
        temp_list.append(list_uniq_keys[i])
        result_list.append(temp_list)
    return result_list

def beaut_view(list_arg):
    for i in range(len(list_arg)):
        list_arg[i][0] = str(list_arg[i][0])
    list_arg = list(map('*'.join, list_arg))
    temp_list =[]
    for item in list_arg:
        if item[0] == '1':
            item = item[2:]
        if item[:2] == '-1':
            item = '-'+item[2:]
        if item[-2:] == '^1':
            item = item[:-2]
        if item[-2:] == '^0':
            item = item[:-4]
        temp_list.append(item)
    temp_str ='+'.join(temp_list)    
    resalt_polinom = temp_str[0]
    for i in range(1, len(temp_str)):
        if not(temp_str[i] == '+' and temp_str[i+1] == '-'):
            resalt_polinom += temp_str[i]
    resalt_polinom += '=0'
    return resalt_polinom

import file_operation as fop

print(fop.file_read('testpol1.txt'))
print(fop.file_read('testpol2.txt'))

resalt = beaut_view(sum_polinoms(fop.file_read('testpol1.txt'),fop.file_read('testpol2.txt')))
print(resalt)
