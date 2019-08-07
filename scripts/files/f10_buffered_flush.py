with open('buffer_test.txt', 'w') as f:
    f.write('Line1\n')
    input('one')
    f.write('Line2\n')
    f.flush()
    input('two')
    f.write('Line3\n')
    input('three')
    
    