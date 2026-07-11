#Count Even and Odd numbers.

numbers = [10, 25, 30, 41, 50]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd) 