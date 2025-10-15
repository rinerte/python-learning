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

class Prey:
    def flee(self):
        print("This animal is fleeing")
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    def run(self):
        print("This rabbit is running")

class Hawk(Predator):
    def fly(self):
        print("This hawk is flying")

class Fish(Prey, Predator):
    def swim(self):
        print("This fish is swimming")

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()