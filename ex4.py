cars = 100 # Declares the cars variable
space_in_a_car = 4.0 # Declares the space in a car variable
drivers = 30 # Declares the drivers variable
passengers = 90 # Declares the passengers variable
cars_not_driven = cars - drivers # Declares value by substracting cars from drivers
cars_driven = drivers # Declares cars_driven with the drivers variable
carpool_capacity = cars_driven * space_in_a_car # Declares the variable by multyplying one variable with another
average_passengers_per_car = passengers / cars_driven # Declares variable by dividing one variable against another


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
