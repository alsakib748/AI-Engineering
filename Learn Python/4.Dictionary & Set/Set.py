# todo; Set

collection = {1,2,3,4, "hello", "world", "world",5}
print(collection)
print(type(collection))
print(len(collection))

# todo; Empty Set

empty_set = set() 
print(empty_set)

collection.add("Sakib")
print(collection)

collection.remove("world")
print(collection)

#  todo; Error Occur, When add 
# collection.add([6,7])
# print(collection) 

collection.pop()
print(collection)

collection.clear()
print(collection)

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))