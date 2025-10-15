# sort

students = [("john", "F", 60),
            ("jane", "B", 70),
            ("dave", "F", 50),
            ("paul", "A", 100),
            ("kate", "A", 90),
            ("lisa", "B", 80)]
students.sort(key=lambda student: student[1]) # sort by grade

for i in students:
    print(i)