#List ka sum nikalo.no sum()
numbers =[]
for i in range(5):
    num = int(input("enter a number :"))
    numbers.append(num)

print(numbers)

total = 0

for i in numbers:
    total += i

print(total)
print(sum(numbers))