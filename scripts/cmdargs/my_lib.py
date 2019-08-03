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

if __name__ == '__main__':     
    a = input_a_number()
    print(__name__)
