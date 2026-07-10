#List reverse karo without reverse().


numbers =[]
for i in range(10):
    num = int(input("enter a number :"))
    numbers.append(num)

print(numbers)
print(len(numbers))
a = (len(numbers))
print(a)


for i in range (a-1, -1, -1):
    print((i) , "--->" , numbers[i])
#     # print(i)
