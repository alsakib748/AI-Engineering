# f = open("D:/AI Engineering/Learn Python/7. File Input-Output/demo.txt", "a")
# # data = f.read(5)
# # data = f.readline()
# data = f.write("\n The topics is patterns in c++")
# print(data)
# print(type(data))
# f.close()

# af = open("D:/AI Engineering/Learn Python/7. File Input-Output/sample.txt", "a")
# af.write("Here is sample")
# af.close()

# with open("D:/AI Engineering/Learn Python/7. File Input-Output/demo.txt", "r") as ff:
#     data = ff.read()
#     print(data)


# with open("D:/AI Engineering/Learn Python/7. File Input-Output/demo.txt", "w") as fff:
#     fff.write("new data")

import os
os.remove("D:/AI Engineering/Learn Python/7. File Input-Output/demo.txt")