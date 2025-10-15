# inheritance
# class Animal:

#     alive = True
#     def eat(self):
#         print("This animal is eating")
#     def sleep(self):
#         print("This animal is sleeping")
    
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")

# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")

# class Hawk(Animal):
#    def fly(self):
#         print("This hawk is flying")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()

# multiple inheritance

# class Prey:
#     def flee(self):
#         print("This animal is fleeing")
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     def run(self):
#         print("This rabbit is running")

# class Hawk(Predator):
#     def fly(self):
#         print("This hawk is flying")

# class Fish(Prey, Predator):
#     def swim(self):
#         print("This fish is swimming")

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# Abstract classes
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is driving")
    def stop(self):
        print("The car has stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("The motorcycle is driving")
    def stop(self):
        print("The motorcycle has stopped")

# vehicle = Vehicle() # will raise an error
car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.go()