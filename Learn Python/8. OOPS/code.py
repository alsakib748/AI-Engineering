# class Student:
#     name = "Sakib"
#     marks = 90
#     def __init__(self, fullname):
#         self.name = fullname
#         print("creating new student in Database..")
#         print(self.name)

#     def welcome(self):
#         print("welcome student")

#     def getMarks(self):
#         return self.marks

# s1 = Student("Ayon")
# s1.welcome()
# print(s1.getMarks())
# print(s1.name)

# class Car:
#     color = "blue"

# car1 = Car();
# print(car1.color)

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi ", self.name, "Your avg score is : ", sum/3)

    # def getName(self):
    #     return self.name

    # def getMark(self):
    #     return self.marks

# s1 = Student("Bangla", 80)
# s2 = Student("English", 90)
# s3 = Student("Math", 90)

s1 = Student("Sakib", [99,98,97])
s1.get_avg()
s1.hello()

# print(s1.getMark())

# average = (s1.getMark() + s2.getMark() + s3.getMark);
# print("Average : ", average)