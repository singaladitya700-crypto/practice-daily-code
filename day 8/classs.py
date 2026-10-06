class Student:
    def __init__(self , name, age , branch):
        self.name = name
        self.age = age
        self.branch = branch

s1 = Student("aditya" , 21 , "Data Science")
s2 = Student("Rahul" , 22 , "Computer")

print(s1.name , s1.age , s1.branch)
print(s2.name , s2.age , s2.branch)