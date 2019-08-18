import urllib.request as request
import random as rn
import numpy as np



image_win = """
  \\O/	
   |
  / \ 
"""
images= [

"""
	   |
	   |
	   |
	   |
 ______|
""",
"""
	---|
	   |
	   |
	   |
 ______|
""",
"""
   |---|
	   |
	   |
	   |
 ______|
""",
"""
   |---|
   O   |
	   |
	   |
 ______|
""",
"""
   |---|
   O   |
   |   |
	   |
 ______|
""",
"""
   |---|
   O   |
  /|   |
	   |
 ______|
""",
"""
   |---|
   O   |
  /|\  |
	   |
 ______|
""",
"""
   |---|
   O   |
  /|\  |
  /	   |
 ______|
""",
"""
   |---|
   O   |
  /|\  |
  / \  |
 ______|
"""
]

main_menu = """
1. Play
2. Rules
3. Exit
"""
def get_word():
	word = None
	try:
		req_obj = request.urlopen('http://tuteurpy.pythonanywhere.com/randomword')
		word = req_obj.read().decode("UTF-8")
		word = word.strip()
	except exception as e:
		print ("Exception getting random word",str(e))
	return word
	
def play_game():
	
	w = get_word()
	#print (w)
	word = list(w)
	#print (word)
	l = len(word)
	h = []
	for i in range(0,l):
		h.append('_')
	
	print (h)
	i=1
	while i <9:
		value = input("Keep guessing and enter the character:")
		if value in word:
			values = np.array(word)
			searchval = value
			ii = np.where(values == searchval)[0]
			#z = word.index(value)
			#print (ii)
			for k in range(0, len(ii)):
						 h[ii[k]] = value
						
			print (h)
			print ()
			if word == h:
				print ("You have won")
				print ("The word is:",''.join(h))
				return
				
			
		else:
			print (images[i])
			i += 1
			print ("Attempts remaining",(9 - i))
			print ()
			if i == 9:
				print ("The word was", w)
				return
			
		
		
def print_rules():
	"""
	Read rules from file rules.txt and print on the screen
	Use file handling for this
	"""
	f = open('rule.txt', 'r')
	for line in f:
			print (line)
	
	
def exit():
	print ("You have succefully exit the game")
	return
	
	
print (main_menu)
x = input("Select the option either 1,2,3:")
if x == '1':
	play_game()
elif x == '2':
	print_rules()
else:
	exit()
