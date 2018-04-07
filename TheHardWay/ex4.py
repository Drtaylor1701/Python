#number of available cars
cars = 100
#amount of seats in each car
space_in_a_car = 4
#number of available drivers
drivers = 30
#number of available passengers
passengers = 90
#number of cars that were not driven because no driver was available
cars_not_driven = cars - drivers
#nubmer of cars driven is equal to the number of drivers because driverless cars are
#totally not a think in this universe
cars_driven = drivers
#total number of seats available
carpool_capacity = cars_driven * space_in_a_car
#average number of passengers in a car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."