def input_list_numbers():
    s = input("Enter list of numbers separated by space : ")
    l = s.split()
    res = []
    for data in l:
        res.append(int(data))
    return res
    
    