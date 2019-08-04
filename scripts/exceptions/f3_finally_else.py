
a = [IndexError, 10, KeyError, ValueError]


for e in a:
    try:
        print('\nRaising', e)
        if e != 10:
            raise e
    except IndexError:
        print("IndexError!!")
    except KeyError:
        print("KeyError!!! ")
        1/0
    else:
        print("No Exception!!!")
    finally:
        print("Finally!!!!!")