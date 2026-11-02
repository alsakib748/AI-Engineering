# todo; Dictionary
info = {
    "key" : "value",
    "name" : "ayon",
    "learning" : "coding",
    "subjects" : ["Python", "C", "Java"],
    "results" : (80, 90, 75),
    "age" : 35, 
    "is_adult" : True,
    "marks" : 94.4,
}

print(info)
print(type(info))
info["name"] = "Sakib"
print(info["name"])
print(info["subjects"])
print(info["age"])

# todo; Null Dictionary
null_dict = {}
print(null_dict)
null_dict['value'] = 100;
print(null_dict)

# todo; Nested Dictionary
student = {
    "name" : "Al Sakib",
    "subjects" : {
        "phy" : 97,
        "che" : 98,
        "math" : 90,
    }
}

print(student)
print(type(student))
print(student["subjects"]["phy"])

# todo; Dictionary Methods

print(student.keys())
print(student.items())
print(student.values())
print(len(list(student.keys())))

pairs = list(student.items())
print(pairs[0])

new_dict = { "city" : "Dhaka"}
student.update(new_dict)

print(student)