cars = 100
drivers = 30
space_in_a_car = 4.0
passenger = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger = passenger / cars_driven

print ("there are", cars, "cars available")
print ("ther are only", drivers, "drivers available")
print ("there will be",cars_not_driven, "empty cars today")
print ("we need to put average", average_passenger, "in each car")

