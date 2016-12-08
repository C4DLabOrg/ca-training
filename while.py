'''
	1. get an input from the user
	2. while loop

'''
jackpot = 4

#while statements
running = True

while running:

	guess = raw_input('This is a guessing game.\nEnter a number :\n')

	#convert the string to an integer
	guess = int(guess)

	#if else statements

	if guess == jackpot:
		print 'You have won!'
		running = False
	elif guess > jackpot:
		print 'You are very far!'
	elif guess < jackpot:
		print 'You are so low'
	else:
		print 'You shouldn\'t reach here'

	print 'Tomorrow, same time'