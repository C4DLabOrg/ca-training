'''
	- Create a function that picks two inputs from a user
	- Create a function that finds the difference between the two values.
	- Create a function that prints the result 
	
'''

#picks inputs from a user
def getInput():
	input1 = int(raw_input('Enter 1st value\n'))
	input2 = int(raw_input('Enter 2nd value\n'))

	return input1, input2

#gets the difference
def getDifference(var1, var2):
	difference = var1 - var2
	return difference

#output results
def output(var):
	print 'The result is ',var


#execute the code
inputs = getInput()

#accessing variables in a tuple
#print inputs[0]
#print inputs[1]

#call function to do the difference
answer = getDifference(inputs[0], inputs[1])

output(answer)

