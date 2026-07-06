#Largest of three numbers

a = int(input("enter a value for a:"))
b = int(input("enter a value for b:"))
c = int(input("enter a value for c:"))

if a > b and a > c:
    print("a is greter than :" , b , "&" , c)
elif b > a and b > c:
    print("b is greter than :" , a , "&" , c)
else:
    print("c is greter than :" , a , "&" , b)
