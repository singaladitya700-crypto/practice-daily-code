student = {
    "name" : "aditya",
    "age" : 20,
    "course" : "python",
    "city" : "pune"
}

print(student["name"])
print(student["age"])

(student["phone"]) = 1234567898
(student["age"]) = 21
del student["city"]
print(len(student))
print(student.keys())
print(student.values())

for k,v in student.items():
    print(k,":",v)

print(student)
