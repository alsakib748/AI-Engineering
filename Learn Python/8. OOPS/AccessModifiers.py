# class Account:
#     def __init_(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.__acc_pass)

class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello()

p1 = Person()

# print(p1.__name)
print(p1.welcome())