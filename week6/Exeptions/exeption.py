#1
def  safe_int(s) :
    try:
        return int(s)
    except ValueError:
        return None
    except Exception:
        return None

#2
def safe_divide(a, b) :
    try:
        return a/b
    except ZeroDivisionError:
        return "undefined"
    
#3

def read_first_line(path):
    try:
        with open(path , "f") as f:
            return f.readline(1)
    except FileNotFoundError:
        return None

#4

def get_value(d, key):
    try:
        return d[key] 
    except KeyError:
        return "missing" 

#5

def parse_ints(values) :
    new_values = []
    for value in values:
        try:
            int(value)
            new_values.append(value)
        except TypeError:
             continue
    return new_values
    
#6

def set_age(age):
    try:
        if age < 0 or age > 150:
            raise ValueError(f"Invalid age: {age}")
        return age
        
    except ValueError as e:
        raise e

#7
class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientFundsError("אין מספיק כסף בחשבון!")
        return balance - amount 
    
    except InsufficientFundsError as e:
        return e
    

#8
def retry(func, n):
    last_error = None
    for i in range(n):
        try:
            return func() 
        except Exception as e:
            last_error = e  

    raise last_error

#9
def count_errors(funcs):
    error_count = 0
    for func in funcs:
        try:
            func() 
        except Exception:
            error_count += 1       
    return error_count

#10
def load_config(path):
    try:
        with open(path, 'r') as file:
            first_line = file.readline()
            return int(first_line)        
    except Exception as e:
        raise RuntimeError("failed to load config") from e 
