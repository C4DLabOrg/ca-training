'''
Create a simple program that uses functions to display the maximum of three numbers a user enters. 

'''

#function for getting user inputs

def getInputs():
	input1 = int(raw_input('Enter the 1st value\n'))
	input2 = int(raw_input('Enter the 2nd value\n'))
	input3 = int(raw_input('Enter the 3rd value\n'))
	
	return input1, input2, input3


# 1st method
def getMax(var):
	maximum = max(var)

	return maximum

#2nd method
def getMaximum(var, var2, var3):

	if var > var2 and var > var3:
		return var
	elif var2 > var and var2 > var3:
		return var2
	elif var3 > var  and var3 > var2:
		return var3

#output function
def display(var):
	print 'The maximum value is ', var

values = getInputs()

print 'All values in the tuple are : ',values 
#answer = getMaximum(values[0], values[1], values[2])
#answer = getMax(values)

display(getMax(values))
