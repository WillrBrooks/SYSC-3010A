import string
import random

secret = [random.choice('ABCDEF') for item in range(4)]

print("I've selected a 4-character secret cde fro the letters A,B,C,D,E,F.")
print("I may have repeated some.")
print("Now, try and guess what I chose.")

yourGuess = []
while list(yourGuess) != secret:
	yourGuess = input("Enter a 4-letter guess: e.g. ABCD : ").upper()
	if len(yourGuess)!=4:
		continue
	
	print("You guessed " +  str(yourGuess))
	
	comparingList = zip(secret, yourGuess)

	correctList = [speg for speg, gpeg in comparingList if speg == gpeg]

	fewestLetters = [min(secret.count(j), yourGuess.count(j)) for j in 'ABCDEF']

	print("Number of correct letters is ", len(correctList))
	print("Number of unused letters is ", sum(fewestLetters) - len(correctList))

print("YOU GOT THE ANSWER : ", secret[0] + secret[1] + secret[2] + secret[3])
