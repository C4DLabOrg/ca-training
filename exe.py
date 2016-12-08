'''
Exercise on String + Constants processing

There are 100 cars
Each car has 4 spaces
There are 30 drivers
There are 90 passengers



1) There will be ___ cars not driven
2) The total capacity for the cars is ___
3) The cars that are being driven are ___
4) Average no. of passengers per driven car is ___
5) If all cars were to be fully filled, there will be 
____ cars driven.

'''

number_of_cars = 100
spaces = 4
drivers = 30
passengers = 90

# There will be ___ cars not driven

cars_not_driven = number_of_cars - drivers
print 'There will be ',cars_not_driven,' cars not driven'

print 'There will be ' + str(cars_not_driven)+ ' cars not driven'

#2) The total capacity for the cars is ___

capacity = number_of_cars * spaces
print 'The total capacity for the cars is ',capacity
print 'The total capacity for the cars is ' + str(capacity)


#3) The cars that are being driven are ___

cars_driven = drivers
print 'The cars that are being driven are ' + str(cars_driven)
print 'The cars that are being driven are ', cars_driven

#4) Average no. of passengers per driven car is ___
avg_passengers = passengers/drivers

print 'Average no. of passengers per driven car is '+ str(avg_passengers)
print 'Average no. of passengers per driven car is ', avg_passengers

#5) If all cars were to be fully filled, there will be ____ cars driven.

print 'If all cars were to be fully filled, there will be '+str(drivers)+' cars driven'
print 'If all cars were to be fully filled, there will be ',drivers,' cars driven'

