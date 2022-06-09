def coding(string_arg):
    string_result = ''
    list_result = []
    n = 1
    for i in range(len(string_arg)-1):
        if string_arg[i] == string_arg[i + 1]:
            n +=1
        else:
            string_result +=  (str(n)+string_arg[i])+','
            n = 1
    string_result += (str(n)+string_arg[i])
    return string_result


def decoding(string_arg):
    list1 = string_arg.split(',')
    string_result = ''
    for i in range(len(list1)):
        string_result += int(list1[i][:-1])*list1[i][-1]
    return string_result



def file_write(file_name, polinom_str):    
    with open(file_name, 'w') as data:
        data.write(polinom_str)


def file_read(file_name):
    data = open(file_name, 'r')
    for line in data:
        polinom = line
    data.close
    return polinom

file_write('base_data.txt', 'aaaaaaaaaaaaaaa1111111111111122222222222222222ccccccccccc')
file_write('code_data.txt', coding(file_read('base_data.txt')))
file_write('decode_data.txt', decoding(file_read('code_data.txt')))

