'''
	Introduction to Data structures : lists

'''
#display results
def display(var):
	print 'Records are : ',var

#defined a list and assigned values to it
names = ['Alex','Ali','Caro']
display(names)


#appending values to a list
names.append('Irene')
display(names)

#delete and item from the list
del names[1]
display(names)
