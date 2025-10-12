# logical_operators

temp = int(input("What is the temperature outside: "))

if not(temp < 0 or temp > 30):
    print("the weather is OK")
    print("go outside!")
elif not(temp>=0 and temp <= 30):
    print("the weather is bad")
    print("stay home!")