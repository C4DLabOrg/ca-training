'''
	for loop
'''


attendees = ['Alex', 'Vicky', 'Caro','Njeri','Joseph', 2]

for name in attendees:
	if name == 'Alex':
		print name, ' was not attentive'
	elif name == 2:
		print name, ' was displaced entry'
	else:
		print name,' came for the Python Training'
