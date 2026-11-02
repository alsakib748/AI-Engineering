# # todo; Function
# def calc_sum(a, b):
#     sum = a + b 
#     print(sum)

# calc_sum(10, 20)
# calc_sum(20, 30)
# calc_sum(30, 40)

# todo; Recursion
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     return fact(n-1) * n

# print(fact(5))

add = 0

def sum(n):
    if (n == 0):
        return 0
    # add += n 
    print(n)
    return sum (n-1) + n

print(sum(5))
# print("Final Summation Result : ", add)