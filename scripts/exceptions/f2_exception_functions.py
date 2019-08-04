
def f1():
    raise IndexError
    
def f2():
    try:
        f1()
        print("After f1")
    except IndexError:
        print("F2 Handling")
   
try:   
    f2()
except ValueError:
    print("Main Value Error")