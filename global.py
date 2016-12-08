'''
	- global variable can be accessed through out the file
 	- local variable is only seen within a function

'''

#local variable
def sayName():
	name = 'Irene'
	print name

sayName()
#print name

#global variable
firstname = 'Njeri'

def shoutName():
	print firstname

shoutName()
