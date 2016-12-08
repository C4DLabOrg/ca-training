'''

Write a program where a user is prompted to specify a range between two numbers and sum all the multiples of 3 within that range. Use functions to write this program.

'''
def get_input():
	input1 = int(raw_input("Enter the first range\n"))
	input2 = int(raw_input("Enter the second range\n"))
	return input1, input2

def range_numbers(value1, value2):
	result = 0
	for numbers in range(value1, value2):
		if numbers%3 == 0:
			print "The numbers are", numbers
			result = sum_numbers(result, numbers)
	return result		

def sum_numbers(var1, var2):
	return var1 + var2

def sum_output(var):
	print "The sum of the numbers is, ", result


inputs = get_input()
result = range_numbers(inputs[0] , inputs[1])
sum_output(result)








	



