#Sum of first N numbers

total = 0
n = int(input("enter a number :"))

for i in range(1, n+1):
    total = total + i

print(total)