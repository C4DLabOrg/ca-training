'''
	
	Write a program that asks a user to choose a word from its list and gives the user the meaning of that word. 

	If the word entered by the user is not in the program's list, the program should alert the user that the word does not exist in the list.

	The program should ask the user whether they want to continue to search for word meanings or else type 'exit' to stop searching.


'''
cities = {
		'Kenya' : 'Nairobi',
		'Uganda': 'Kampala',
		'Rwanda': 'Kigali',
		'Tanzania' : 'Dodoma' 
	}


#get input from a user
def getInput():
	find = raw_input('Enter a Country to search its capital or exit to Quit\n')
	return find

#search function
def search(var):

	for key in cities:
	 	if key == var:
	 		status = cities[key]
	 		break
	 	else:
	 		status = 'not found'

	return status

def finder():

	running = True

	while running:
		userInput = getInput()
		
		if userInput == 'exit':
			running = False
		else:
			value = search(userInput)

			if value != 'not found':
				print 'The city is ',value
			else:
				print 'Not Found'

		
finder()










	
