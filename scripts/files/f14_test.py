import sys

if len(sys.argv) == 3:
    with open(sys.argv[1], 'r') as f1:
        with open(sys.argv[2], 'w') as f2:
            f2.write(f1.read())
else:
    print("Need 2 args")