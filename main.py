# sort

students = [("john", "F", 60),
            ("jane", "B", 70),
            ("dave", "F", 50),
            ("paul", "A", 100),
            ("kate", "A", 90),
            ("lisa", "B", 80)]
students.sort(key=lambda student: student[1]) # sort by grade
reversed_students = sorted(students, key=lambda student: student[1], reverse=True) # sort by grade descending

# for i in students:
#     print(i)

# MAP - applies a function to all items in an iterable
# 

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
store_euros = list(map(to_euros, store))

# for i in store_euros:
#     print(i)


# Filter - creates a collection of elements from an iterable for which a function returns true
#filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

old_enough = lambda data: data[1] >= 18
drinking_buddies = list(filter(old_enough, friends))

for i in drinking_buddies:
    print(i)