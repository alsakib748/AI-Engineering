class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    # def __init__(self, name):
    #     self.name = name
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.start())

car1 = Fortuner("Diesel")
car1.start()

car2 = ToyotaCar("Prius", "electric")
print(car2.type)

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC);
# print(c1.varB);
# print(c1.varA);