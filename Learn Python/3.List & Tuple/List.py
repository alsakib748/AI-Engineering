marks = [90, 70, 65, 50, 55]
print(marks)
print(marks[0])
print(marks[3])
print(type(marks))

student = ["Sakib", 90, 26, "Dhaka"];
print(student)

# todo; List Slicing
print(student[1:2])

# todo; List Negative Slicing
print(student[-2:-1])

# todo; List Methods

student.append("3.81")
print(student)

# marks.sort()
marks.sort(reverse=True)
print(marks)

# todo; Reverse 
student.reverse()
print(student)

# todo; insert value specific index
student.insert(2, 'BUBT') 
print(student)

# todo; remove
marks.remove(55)
print(marks)

# todo; pop
student.pop(2)
print(student)
