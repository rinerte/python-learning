# lambda function = function written in 1 line using the lambda keyword
#                      accepts any number of arguments, but only has one expression
#                      (think of it as a shortcut)
#                      (useful if needed for a short period of time, throw-away)

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first, last: first + ' ' + last
age_check = lambda age: True if age >= 18 else False

print(double(5))
