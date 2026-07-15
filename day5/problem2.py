# def largest(a,b,c):
#     if a > b and a > c:
#         return a ," is greater"
#     elif b > c and b > a:
#         return b ," is greater"
#     else:
#         return c ," is greater"
    
# print(largest(10,33,2))


def largest(*numbers):

    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest
        
greatest = largest(10,20,30,43,55,67,42,1)
print(greatest)