#List me largest number bina max() use kiye find karo.

numbers =[]
for i in range(5):
    num = int(input("enter a number :"))
    numbers.append(num)

print(numbers)

largest = numbers[0]

for big in numbers:
    if big > largest:
        largest = big

print("largest is" ,largest)

#smallest number in list without using min()

smallest = numbers[0]

for small in numbers:
    if small < smallest:
        smallest = small
print("smallest is" , smallest)