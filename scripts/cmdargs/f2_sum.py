import sys

# check the type before converting to int
if len(sys.argv) == 3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        print( int(sys.argv[1]) + int(sys.argv[2]) )
    else:
        print("Enter valid integers")
else:
    print("Expected 2 arguments, given ", len(sys.argv) -1 )
