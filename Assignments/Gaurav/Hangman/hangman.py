import urllib.request as request
from functools import reduce

def get_word():
	word = None
	try:
		# Replace with your URL here
		req_obj = request.urlopen('http://tuteurpy.pythonanywhere.com/randomword')
		word = req_obj.read().decode("UTF-8")
		word = word.strip()
	except Exception as e:
		print("Exception getting Random word", str(e))
	return word


# Use this in case the Web API doesn't work, copy the wordgenerator from RandomWordWeb API project
"""
from wordgenerator import RandomWordGenerator

rw = RandomWordGenerator()
print(rw.get_word())
# use rw.get_word() to get random words instead of get_word()
"""


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
  /    |
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

def print_stats(word, guess,turns_left):
	"""
	Print stats for each turn
	Example:
	Word : _ _ a _ b _ c _ _
	Correct : [a, c, b]
	Incorrect : [x, q, w, d]
	"""
	print("Remaining Turns: %2d \t\t Guesses : %s" %(turns_left,','.join(guess)) )
	print("Word :", ' '.join(word))

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
	word_to_guess = get_word()
	word_to_guess = word_to_guess.upper() # we will keep both input and the word in lower case
	
	max_turns = len(images) - 1
	guess_str = ['_'] * len(word_to_guess)
	guess_till_now = []
	
	current_turn = 0
	win = False
	
	while current_turn < max_turns:
		print_stats(guess_str, guess_till_now, max_turns - current_turn)
		# convert input to upper case
		choice = input("Guess alphabet or full word: ").upper()
		print()
		print()

		if len(choice) == 1: # user enters only one character to guess
			if choice in guess_till_now:
				continue
			else:
				if choice in word_to_guess:
					guess_till_now.append(choice)
					s = sum([1 if c in guess_till_now else 0 for c in word_to_guess])
					win = (s == len(word_to_guess))
				else:
					guess_till_now.append(choice)
					current_turn += 1

				# update the word to be printed
				for i in range(len(word_to_guess)):
					if word_to_guess[i] == choice:
						guess_str[i] = choice
		else: # player guesses entire word
			if word_to_guess.upper() == choice:
				win = True
			else:
				break
		if win:
			break
		print(images[current_turn])
	if win:
		print(image_win)
		print("You WINNN!! Word is '", word_to_guess, "'")
	else:
		print("You LOOSE!!")
	input()
		
def print_rules():
	"""
	Read rules from file rules.txt and print on the screen
	Use file handling for this
	"""
	with open("rules.txt", 'r') as f:
		for line in f:
			print(line, end = '')


def main():
	"""
	Print the menu here and based on the menu input given by user, call other functions.
	Use take_input_int function from my_lib
	"""
	while True:
		print(main_menu)
		choice = input("Enter Choice (1-3): ")
		print()
		print()
		if not choice.isdigit():
			print("Enter a valid Choice Number")
		elif int(choice) == 1:
			play_game()
		elif int(choice) == 2:
			print_rules()
		elif int(choice) == 3:
			exit()
		else:
			print("Enter valid Input")
main()