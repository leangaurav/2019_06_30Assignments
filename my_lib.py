def input_list_numbers():
    s = input("Enter list of numbers separated by space : ")
    l = s.split()
    res = []
    for data in l:
        res.append(int(data))
    return res

def input_a_number():
    """
    input a number and return it as an integer
    the function checks validity of input.
    if input is not correct, it keeps on asking for input
    till user enters correct.
    """
    while True:
        n = input("Enter a number:")
        if n.isdigit():
            return int(n)

def input_a_float():
    while True:
        n = input("Enter a float:")
        try:
            r = float(n)
            return r
        except ValueError:
            pass

def input_a_float_wrong():
    while True:
        try:
            n = input("Enter a float:")
            r = float(n)
            return r            
        except BaseException: # except:
            pass
            
if __name__ == '__main__':     
    a = input_a_float_wrong()
    print(__name__)

    