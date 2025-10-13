# function = a block of code which is executed only when it is called

# def repeat(name, last_name,rep_func):
#     print("Hello "+name+" "+last_name)
#     for i in range(10):
#         rep_func()

# def print_exclamation():
#     print("!", end="")

# repeat("Name", "Last Name", print_exclamation)

# def multiply(number1, number2):
#     return number1*number2

# x = multiply(6,8)

# print(x)

# ARGS parameter = *args = parameter that will pack all arguments into a tuple

# def add(*arguments):
#     sum = 0
#     for x in arguments:
#         sum+=x
#     return sum

# print(add(4,7,2,5,34,4,62,8,6,2,6,43,3234,3))

# **kwargs = parameter that wilol pack all arguments into a dictionary

# def hello(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)

# hello(kick="Kick",twitch="Twitch",youtube="Youtube")

word = "Moon"
print("The {}".format(word))

