'''
Write a Python program which iterates the integers from 1 to 50. For multiples of 3 print 'Fizz' instead of the number and for multiples of 5 print 'Buzz'. Numbers which are multiples of both 3 and 5 print 'FizzBuzz'
'''
for numbers in range(1,51):
	if numbers%3 == 0 and numbers%5 == 0:
		print "FizzBuzz"

	elif numbers%3 == 0:
		print "Fizz"

	elif numbers%5 ==0:
		print "Buzz"

	else:
		print "Number not multiple of 3 or 5"
		print numbers


'''
Sample Output

FizzBuzz
1
2
Fizz
4
buzz 
'''