#Second Largest Number

numbers = [10,40,30]

largest = numbers[0]
second_largest = 0

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(largest)
print(second_largest)

