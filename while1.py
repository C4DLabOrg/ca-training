
#temperature = 25

temperature = int(raw_input('Get the temperature\n'))

while temperature > 15:
	print temperature, ' Still seems high'
	temperature = temperature - 1
	

print 'now that is cool enough'
