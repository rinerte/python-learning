from car import Car



car_1 = Car("Toyota", "Camry", 2020, "Blue")
car_2 = Car("Honda", "Civic", 2019, "Red")
car_3 = Car("Ford", "Mustang", 2021, "Black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

# Print list of method and attributes available in Car class

print(dir(Car))