student = {
    "Aditya": 95,
    "Rahul": 88,
    "Aman": 91
}

name = input("enter a name:")
marks = student.get(name)

if marks is None:
    print("student data not found")
else:
    print("Marks :" , marks)