'''
	Sample implementation of a tuple.

	they are immutable
'''

def display(var):
	print var

#define a tuple
shoplist = ('milk', 'sugar','salt')
#display(shoplist)

newshoplist = ('honey','tea bags')

bothlists = shoplist + newshoplist
#display(bothlists)

anotherTuple = ('books','pens',bothlists)
#display(anotherTuple)

''' 
 for i in anotherTuple:
	display(i)
'''

display(anotherTuple)
display(anotherTuple[2])

print 'length is : ',len(anotherTuple)
print 'length is : ',len(anotherTuple[2])

print 'Both lists are of length', len(anotherTuple) + len(anotherTuple[2]) - 1





