def sum_of_value(dic):
    sum_value = 0
    for v in dic.values():
        sum_value += v 
    return sum_value

#2
def Key_with_maximum_value(dic):
    maximum_value = 0 
    max_v = 0
    max_k = ""
    for k , v in dic.items():
        if max_v < v :
            max_v = v
            max_k = k
    return max_k

#3
def count_characters(word):
    dict_count = {}
    for char in word : 
        if char not in dict_count:
            dict_count[char] = 1
        else:
            dict_count[char] += 1
    return dict_count
#4
def ivert_a_dictionary(dic):
    new_dic = {}
    for k , v in dic.items():
        new_dic[v] = k
    return new_dic

#5
def merge_two_dictionaries(dict1, dict2):
    return dict1 | dict2

#6
def filter_by_value(dict,vlue):
    new_dic = {}
    for k , v in dict.items():
        if v > vlue:
            new_dic[k] = v
    return new_dic

#7
def group_by_first_letter(words):
    grouped = {}
    for word in words:
        if word:
            grouped.setdefault(word[0], []).append(word)
    return grouped

#8
def word_frequency(text):
    frequencies = {}
    for word in text.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

#9
def common_keys(dict1, dict2):
    comon_keys = []
    for k in dict1:
        if k in dict2:
            comon_keys.append(k)
    return sorted(comon_keys)     

#10
def most_frequent_value(dict):
    new_dict = {}
    for v in dict.vlues() : 
        if v not in new_dict:
            new_dict[v] = 1
        else:
            new_dict[v] += 1
    max_v = 0 
    max_k = 0
    for k , v in new_dict.items():
          if max_v < v :
            max_v = v
            max_k = k
    return max_k