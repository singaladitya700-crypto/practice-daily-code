#employee salary

employee = {
    "Rahul": 30000,
    "Aman": 45000,
    "Aditya": 50000
}

name = input("enter a name:")

unknown = employee.get(name)

if unknown is None:
    print("Employee not found")
else:
    salary = int(input("enter a salary :"))
    employee[name] = salary
    print(employee)