'''
>>> The Calculator assignment

1) Take three inputs from a user : a, b, c 
2) a and b should be operands to perform arithmetic
   operations
3) c should be the choice of operation the user would
   want to perform. (+, -, %, *, **)
4) Calculate and print each output for the operations

5) get records from the user until the user enters 
   'end' to stop the program

'''
running = True

while running:

	inputA = int(raw_input('Enter 1st Operand\n'))
	inputB = int(raw_input('Enter 2nd Operand\n'))
	operator = raw_input('Enter the operation to perform\n')

	if operator == '+':
		print 'Sum is ', (inputA + inputB)
	elif operator == '-':
		print 'Subtraction is ', (inputA - inputB)
	elif operator == '%':
		print 'Remainder is ', (inputA % inputB)
	elif operator == '*':
		print 'Multiplication is ', (inputA * inputB)
	elif operator == '**':
		print 'Power is ', (inputA ** inputB)
	else:
		print 'Operator not defined'

	end = raw_input('Enter end to exit or press enter to continue\n')
	if end == 'end\n':
		running = False








