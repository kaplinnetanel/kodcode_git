#1
def sum_of_tuple(tpl):
    sum_tuple = 0 
    for num in tpl:
        sum_tuple += num
    return sum_tuple

#2
def max_element_in_tuple(tpl):
    max_tuple = 0
    for num in tpl:
        if num > max_tuple:
            max_tuple = num
    return max_tuple        

#3
def count_occurrences(tpl,value):
    count = 0
    for num in tpl:
        if num == value:
            count += 1
    return count

#4
def revers_a_tuple(tpl):
    new_tuple = []
    for i in range(1,len(tpl)+1):
        new_tuple.append(tuple[-i])        
    return tuple(new_tuple)

#5
def swap_pairs(tpl):
    new_tuple = []
    for i in range(0,len(tpl),2):
        new_tuple.append(tpl[i+1])
        new_tuple.append(tpl[i])
    return new_tuple

#6
def mini_and_max(tpl):
    mini = 0
    maxi = 0
    for num in tpl:
        if num > maxi:
            maxi = num
        elif num < mini:
            num = num 
    return (mini , maxi)   

#7
def distance_between_points(tpl1,tpl2):
    x1 , x2 = tpl1
    y1 , y2 = tpl2
    return(((x2 -x1)**2+ (y2 - y1)**2)**0.5)

#8 
def merge_and_sort(tpl1 , tpl2):
    merge = list(tpl1 + tpl2)
    n = len(merge)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if merge[j] < merge[min_index]:
                min_index = j
        merge[i], merge[min_index] = merge[min_index], merge[i]    
    return merge
#9
def frequency_table(tpl):
    dic = {}
    for num in tpl:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    return tuple(dic.items())

#10
def rotate_tuple(tpl, k):
    n = len(tpl)
    if n == 0:
        return tpl
    k = k % n
    return tpl[-k:] + tpl[:-k]




    
