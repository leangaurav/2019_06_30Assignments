import my_lib

print(dir(my_lib))
print("Other file")
print(__name__, my_lib.__name__)

my_lib.add(10,1111)

from my_lib import sub

sub(100,30)