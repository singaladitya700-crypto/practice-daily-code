#Largest of two numbers

a = int(input("enter a number:"))
b = int(input("enter a number:"))

if a > b:
    print(a , "is larger than" , b)
elif b > a:
    print(b , "is larger than" , a)
else:
    print("both are equal")