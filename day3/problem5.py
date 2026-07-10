#Smallest number without min()

numbers = []

for i in range(5):
    num = int(input("enter a number :"))
    numbers.append(num)

print(numbers)

smallest = numbers[0]

for small in numbers:
    if small < smallest:
        smallest = small

print("smallest number is" , smallest)