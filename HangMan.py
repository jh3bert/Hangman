from random_word import RandomWords   

hangman = ['__ \n  | \n', 
'__ \n  | \n  O', 
'__ \n  | \n  O\n  |', 
'__ \n  | \n  O\n  |\n  |',
'__ \n  | \n  O\n  |\n  |\n /',
'__ \n  | \n  O\n  |\n  |\n / \\',
'__ \n  | \n  O\n \\|\n  |\n / \\',
'__ \n  | \n  O\n \\|/\n  |\n / \\ ']

print("Let's play some HangMan")

letters = int(input("Enter length of word 5-10 to play with! "))

if (letters < 5):
	letters = 5

elif(letters >10):
	letters = 10


w = RandomWords()
string = w.get_random_word(minLength = letters, maxLength = letters)

#print(string)

hangSlots =[]
for x in range(letters):
	hangSlots.append('_')

wrongAnswers = 0
correctAnswers = 0
correctAmt = 0

while (wrongAnswers < 7 and correctAnswers < letters):
	print(hangman[wrongAnswers])
	print()
	print(hangSlots)
	guess = input("Guess a Letter! ")

	for x in range(letters):
		if(string[x] == guess[0]):
			hangSlots[x] = guess[0]
			correctAmt += 1
	if (correctAmt > 0):
		print("Nice! There was {0} occurences of letter {1}".format(correctAmt, guess[0]))
		correctAnswers += correctAmt
		correctAmt = 0
	else:
		print("There are no {0}'s in the word.\n{1}".format(guess[0], hangSlots))
		wrongAnswers += 1


if (wrongAnswers == 7):
	print(hangman[wrongAnswers])
	print()
	print(hangSlots)
	print("You lose! The Word was: ")
	print(string)
elif (correctAnswers == letters):
	print(hangman[wrongAnswers])
	print()
	print(hangSlots)
	print("Boom! You did it.")
