# todo; While Loops

# count = 1
# while count <= 5:
#     print("Sakib")
#     count += 1

# n = int(input("Enter the n value : "))
# i = 1
# value = 0
# while value < 30:
#     value = n * i
#     # print(n * i)
#     print(value)
#     i += 1

# i = 1
# while i <= 10:
#     result = i * i
#     print(result)
#     i += 1

# data = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# search_number = int(input("Enter the search number : "))
# # print(data[3])
# notFound = False
# i = 0
# while i < len(data): 
#     if(search_number == data[i]):
#         notFound = True
#         print("Data found on Index of ", i)
#         break
#     i += 1


# if(notFound == False):
#     print ("Data not found")

# todo; For Loop

# number = [1,2,3,4,5]

# for num in number:
#     print(num) 

# veggies = ["potato", "brinjal", "strawberry"]

# for veg in veggies:
#     print(veg)

# tup = (1,2,4,5,6)

# for t in tup:
#     print(t)

# str = "Al Sakib Ayon"
# for s in str:
#     print(s)
# else: 
#     print("Work Done")

# todo; Range

# print(range(5)) 
# for i in range (10): 
#     print(i)

# for i in range (2,10): # range(start, stop)
#     print(i)

# for i in range (2, 10, 2): # range(start, stop, step)
#     print(i)

# for i in range (2, 100, 2): # range(start, stop, step)
#     print(i)

# for i in range (1, 101, -1): # range(start, stop, step)
#     print(i)

# for i in range (100, 0, -1): # range(start, stop, step)
#     print(i)

# for i in range (5): # range(start, stop, step)
#     pass
# print("End of task")

# n = 5
# sum = 0
# for i in range (1, n+1): # range(start, stop, step)
#     sum += i
#     print(i)

# print("Total sum : ", sum)

i = 1
n = int(input("Enter the n number : "))
fact = 1;
while( i <= n):
    fact *= i
    i += 1

print("Factorial : ", fact)