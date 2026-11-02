# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True 
#         self.acc  = True
#         print("Car Started ..")

# car1 = Car()
# car1.start()

class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc 

    # debit
    def debit(self, amount):
        self.bal -= amount 
        print("Tk. ", amount, "was debited")
        print("Total balance = ", self.get_balance())

    # credit
    def credit(self, amount):
            self.bal += amount 
            print("Tk. ", amount, "was credited")
            print("Total balance = ", self.get_balance())

    # final balance
    def get_balance(self):
        return self.bal


acc1 = Account(500, 12345)
acc1.credit(500)
acc1.debit(500)
acc1.get_balance()