def ascen_seq(list_arg):
    result_list = []
    temp = list_arg[0]
    for i in range(len(list_arg)-1):
        result_list1 = []
        if temp > list_arg[i]:
            temp = list_arg[i]
        result_list1.append(temp)
        k = 0
        for j in range(i, len(list_arg)-1):
            if result_list1[k] < list_arg[j+1] and list_arg[j+1] < max(list_arg[(j+1):]):
                result_list1.append(list_arg[j+1])
                k +=1            
        if   list_arg[-1] >  result_list1[-1]:
            result_list1.append(list_arg[-1])
        if len(result_list) < len(result_list1):
            result_list = result_list1
        temp = result_list1[0]
    return result_list



print(ascen_seq([2,1,5,9,4,5,2,3,6,7,12,1,2,3,10,11]))
