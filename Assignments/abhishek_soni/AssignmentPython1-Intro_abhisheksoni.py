# Python Assignment:

# Question:1 

	s1 = 'abhishek'
	s2 = 'abhisghek.soni22@gmail.com'
	print(len(s1)),print(len(s2))

	# Output

	8 26
	(None, None)

	s1 = 'abhishek'
	s2 = 'abhisghek.soni22@gmail.com'
	print(len(s1),len(s2))

	# Output
	8 26

# Question: 2 - WAP to input a string and print its length.

	s = input ("Enter a string:")
	print(len(s))

# Question: 3 - WAP to input 2 numbers and print their sum and difference.
	s1 = input("Enter first number: ")
	s2 = input("Enter second number: ")
	x = int(s1) + int(s2)
	y = int(s1) - int(s2)
	print("sum of the numbers: ",x) 
	print("diff of the numbers: ",y) 

# Question 5 - Predict output:
	s1 = 'ab'
	s2 = 'de'
	s3 = s1 + s2
	print(s3)

	# output:
	abde

# Question: 6 - Predict output:
	s1 = 'ab'*4
	print(s1)
	# output:
	abababab

# Question: 7 - Predict output:
	s1 = 'ab\n'*4 # '\n' is for next line
	# output:
	ab
	ab
	ab
	ab

# Question: 8 - WAP to input a string s and a number n. Print the string n times on the screen, each should appear in a separate line (do not use any kind of loops, use the multiplication operator).

	s = input ("enter a string: ")
	n = int(input ("enter a number: "))
	n = int(n)
	y = (s + '\n') * n
	print(y)

	# Output:
	enter a string: abc
	enter a number: 3
	abc
	abc
	abc

# Question: 9 - Predict Output:

	res = print('abhishek')
	print(res)
	print(type(res))
	# Output:
	abhishek
	None
#	<class 'NoneType'>

# Question: 10 - Predict Output:
	res = len('tuteur.py@gmail.com')
	print(type(res)
	# Output:
#	<class 'int'>

# Question: 11 - Predict Output:
	s1 = 'gaurav'
	s2 = 'tuteur.py@gmail.com'
	s3 = s1 + '\n' + s2
	print(type(s3))
	print(len(s3))
	# Output:
#	<class 'str'>
	26

# Question: 12 & 13
	n = int(input("Enter a number: " ))
	s = math.sqrt(n)
	print(s)
	# how to import and use sqrt ??

# Question: 14 - WAP to input 4 numbers from user and print their average
	s1=int(input("Enter a first number:"))
	s2=int(input("Enter a second number:"))
	s3=int(input("Enter a third number:"))
	s4=int(input("Enter a fourth number:"))
	average=(s1+s2+s3+s4)/4.0
	print(average)

# Question: 15 - Use the help function to check what the abs function in python does.
	help(abs)
	abs(x, /)
	    Return the absolute value of the argument.

# Question: 16. What is the output of this code when run from python interpreter.
	>>> print(__name__)
	__main__

# Question: 17. What is the output of this code when run from python script.
	(base) {"message"::Desktop abhishekkumars$ python3 print\(_name_\).py
	__main__
	(base) {"message"::Desktop abhishekkumars$


#Question: 18 - Does the dir of int class contain an attribute __name__ (Y/N).
 no 

#Question: 19
>>> print(__name__)
__main__
>>> print(__builtins__.__name__)
builtins
>>> print(int.__name__)
int














