#pattern printing

rows = int(input("enter a number :"))

for i in range(1 , rows+1):
    for j in range(1 , i+1):
        print("*" , end = " ")

    print()