#1
def remove_duplicates(numbers : list):
    return set(numbers)

print(remove_duplicates([1,1,1,3,4,5,5,6,7,7,8]))

#2
def count_unique_elements(numbers : list):
    new_s = set(numbers)
    count = 0
    for n in new_s:
        count += 1
    return count

#3
def common_elements(list1, list2):

    return sorted(list(set(list1) & set(list2)))

#4
def elements_in_only_one(list1,list2):
    return list(set(list1) | set(list2))
            

#5
def is_subset(list1 ,list2):
    return set(list1) <= set(list2)

#6
def unique_characters(word):
    b = True
    for ch in word:
        if ch not in set(word):
            b = False
    return b          
    
#7
def first_repeated_element(lst):
    seen = set()
    
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
        
    return None

#8
def distinct_words(word):
    words = word.split()
    return len(words)

#9
def pair_sum_exists(lst, target):
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
        
    return False

#10
def symmetric_difference_custom(list1, list2):
    result = []
    
    for item in list1:
        if item not in list2:
            result.append(item)
            
    for item in list2:
        if item not in list1:
            result.append(item)
            
    return sorted(list(set(result)))
