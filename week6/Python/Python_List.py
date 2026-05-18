#1
def sum_of_a_list(numbers : list):
    count_num = 0 
    for num in numbers:
        count_num += num
    return count_num

#2
def maximum_element(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

#3
def count_occurrences(numbers , value):
    cuont_value = 0 
    for num in numbers:
        if num == value:
            cuont_value += 1
    return cuont_value

#4
def reverse_a_list(numbers : list):
    new_list = []
    for n in range(len(numbers)):
        new_list.append(numbers.pop())
    return new_list

#5
def remove_duplicates(numbers: list):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list

#6
def second_largest(numbers):
    max_num = 0
    second_num = 0 
    for num in numbers:
        if num > max_num:
            second_num = max_num
            max_num = num 
        elif max_num > num > second_num:
                second_num = num 
    if second_num == max_num :
        return None                
    return second_num

#7
def merge_two_sorted_lists(numbers1 ,numbers2):
    new_numbers =[]
    ind1 = 0
    ind2 = 0
    while ind1 < len(numbers1) and ind2 < len(numbers2) :
        if numbers2[ind2] > numbers1[ind1]:
            new_numbers.append(numbers1[ind1])
            ind1 += 1
        else:
            new_numbers.append(numbers2[ind2])
            ind2 += 1 
    new_numbers.append(numbers2[-1])           
    return new_numbers

#8
def rotate_list(numbers, k):
    for i in range(k):
        last = numbers.pop()
        numbers.insert(0, last)
    return numbers
print(rotate_list([1,2,3,4,5], 2))