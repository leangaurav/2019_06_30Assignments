class Selfmanaged:
    num_obj=0
    def __init__(self):
        Selfmanaged.num_obj+=1
        print("Created: Current Count: ", Selfmanaged.num_obj)
    def __del__(self):
        Selfmanaged.num_obj-=1
        print("Deleted: Current Count: ", Selfmanaged.num_obj)
    def get_current_count(self):
        return Selfmanaged.num_obj
        
s1=Selfmanaged()
s2=Selfmanaged()
print(s1.get_current_count())