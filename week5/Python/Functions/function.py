#1
def is_even(num : int ) -> bool:
    """return true if num is even , False otherwise"""
    return num % 2 == 0 

#2
def factorial(n):
    """return factorial that n! """
    result = 1 
    for num in range(1,n + 1):
       result *= num 
    return result
        
#3
vowels = "iuoea"
def count_vowels(s) -> int:
    """returns the number of vowels in string"""
    count = 0 
    for word in s:
        if word in vowels:
            count += 1
    return f"the number of vowels in string {count}" 
       
#4
def reverse_string(s) -> str:
    """That returns the string reversed"""
    return s[::-1]

#5
def find_max(lst) -> int :
    """the returns the largest number"""
    max = 0 
    for num in lst:
        if num > max:
            max = num 
    return f"this is the largest number{max}"

#6
def celsius_to_fahrenheit(c):
    """that converts Celsius to Fahrenheit. """
    return c * 1.8 + 32
 
#7
def is_palindrome(s) -> bool:
    """return True if the string reads the same forwards and backwards """
    return s == s[::-1]

#8
def list_even(list) ->list:
    """returns a new list with only the even numbers""" 
    return [num for num in list if num % 2 == 0]

#9
def c_anagrement(str1 , str2)-> bool:
    """returns True if they are anagrams of each other."""
    return sorted(str2) == sorted(str1)

#10 
def count_word(s)-> dict:
    """that counts how many times each word appears in a sentence and returns a dict. """
    new_dict = {}
    sentens = s.split()
    for word in sentens: 
        if word in new_dict:
             new_dict[word] += 1
        else:     
            new_dict[word] = 1
    return new_dict        

#11
def calculate_resource_drain(cost, waste_factor):
    """return the amount of resources lost to inefficieny"""
    return cost * waste_factor

def get_net_resources(cost, waste_factor):
    """ returns the final resource count after accounting for the drain"""
    return cost - calculate_resource_drain(cost , waste_factor)

#12

def intercept_length(packet):
    """returns the character count of an intercepted transmission."""
    return len(packet)

def verify_transmission(packet)-> None:
    """Validating raw data packets through a dedicated verification sub-routine. """
    length = intercept_length(packet)
    print(f"Intercepted packet contains {length} bytes of data.")

#13
import math
def convert_to_decibels(signal_strength):
     dB= 20*math.log10( signal_strength/1 )
     return dB

def is_threat_detected(signal_strength) :
    if convert_to_decibels(signal_strength) > 90:
        return True
    return False

#14

def get_fuel_surcharge(distance):
     return ((distance /10 )*8)*0.17 
   

def get_hazard_pay(distance):
    return (distance / 10) * 8 * 0.05

def calculate_mission_cost(distance):
    return get_hazard_pay(distance) + get_fuel_surcharge(distance) + (distance / 10) * 8 