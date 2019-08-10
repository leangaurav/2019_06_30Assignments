# Complete this template

import urllib.request as request
import string
image_win = """
 \ O /	 |
   |   |
  / \  |
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

Enter your option : """
def show_menu():
	#print( main_menu)
	
	while True:
		opt=int(input(main_menu))
		if opt in (1,2,3):
			if opt==1:
				print(play_game())
			elif opt==2:
				print(print_rules())
			elif opt==3:
				break
		else:
			print('Invalid option !!')
	
def play_game():
	"""
	- Write the Game Logic here
	- set the number of max turns to the number of images available.
	- get a random word using the get_word() function.
	- mantain the gusses (_ _ a _ _ b _) as a list of strings
	- Print one image and current status using print stats and ask user to enter an alphabet 
	- Use input_word() from my_lib to input one or more character
	- If user enter a character, check depending on whether it exists in the word, update correct and incorrect guess lists.
	- If user enters a word, user wins if the word is correct and looses directly if the word is wrong, irrespective of the number of remaining lives/chances.
	- If user enters a character that has already been entered, ignore it irrespective of correct or incorrect
	- Increase the turn count each time user guesses wrong.
	- Repeat till user wins or looses(guesses wrong or number of turns becomes 0)
	"""
	max_turn=len(images)-1
	missed,guesses,turns,success=[],[],0,False
	rand_word=get_word()
	word=list(('_'*len(rand_word)))
	#print(rand_word)
	#print('\nword: \n',' '.join(word))
	while turns<len(images)-1:
		
		print('Remaining turns: ',max_turn, end='	')
		print('Guesses: ', ','.join(guesses))
		print('\nword: \n',' '.join(word))
		guess=input_word()
		if guess not in guesses:
			guesses.append(guess)
		#print(guess)
		#print(guesses)
		i=0
		for c in rand_word:
			if c==guess:
				word[i]=c
				
			i+=1
		if guess==rand_word or ''.join(word)==rand_word:
			print('\nCongrats, you have won!!\n')
			success=True
			print(image_win)
			break
				
		if guess not in rand_word:
			if guess not in missed:
				missed.append(guess)
				print(images[turns])
				max_turn-=1
				turns+=1
	if not success:
		print('You killed a man, word was ',rand_word.upper())
def input_word():
	"""
	input a number and return it as an integer
	the function checks validity of input.
	if input is not correct, it keeps on asking for input
	till user enters correct.
	"""
	while True:
		n = input("Guess a letter or complete word: ")
		if n.isalpha():
			return n	
			
def print_rules():
	with open('rules.txt','r') as f:
		return f.read()
	
def get_word():
		word=None
		try:
			req_obj=request.urlopen('http://tuteurpy.pythonanywhere.com/randomword')
			word=req_obj.read().decode("UTF-8")
			word=word.strip()
		except Exception as e:
			print("exception getting random word", str(e))
		return word
if __name__=='__main__':
#			print(get_word())
#			print(print_rules())
			
			print(show_menu())