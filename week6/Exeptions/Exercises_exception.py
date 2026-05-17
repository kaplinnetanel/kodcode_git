#1
def safe_int(s):
    try:
        return int(s)
    
    except Exception:
        return None

#2

def safe_divide(a, b):
    try :
        return a / b
    except ZeroDivisionError:
        return "undefined"

#3

def read_first_line(path):
    with open (path ,f) as f:
        try:
            return f.readline(1)
    