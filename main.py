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

# MAP 

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
