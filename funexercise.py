'''

Write a program where a user is prompted to specify a range between two numbers and sum all the multiples of 3 within that range. Use functions to write this program.

'''

#get inputs from a user
def getInputs():
	input1 = int(raw_input('Enter 1st value\n'))
	input2 = int(raw_input('Enter 2nd value\n'))

	return input1, input2

#adds two numbers
def addition(var1, var2):
	result = var1 + var2

	return result

#print outputs
def output(var, var2, var3):
	print 'The summation of multiples of 3 between {0} and {1} is {2}'.format(var2, var3, var)

#get multiples
def getMultiples(var1, var2):
	
	result = 0
	for var in range(var1, var2):
		if var%3 == 0:
			#result = result + var
			result = addition(result, var)
	return result

'''
	Now we want to call all the functions in order
	
'''
  
fromUser = getInputs()

answer = getMultiples(fromUser[0], fromUser[1])


output(answer, fromUser[0], fromUser[1])

