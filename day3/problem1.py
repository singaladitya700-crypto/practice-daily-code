#User se 5 numbers input lo aur list me store karo.

#method 1 using while

numbers =[]
while len(numbers) < 5:
    a = int(input("enter a number :"))
    numbers.append(a)

print(numbers)

#method 2 using for and pythonic

numbers =[]
for i in range(5):
    num = int(input("enter a number :"))
    numbers.append(num)

print(numbers)

