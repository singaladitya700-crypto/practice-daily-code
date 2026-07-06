# while loop

a = 1
while a < 10:
    print(a)
    if a == 7:
        break
    a = a + 1


a = 0
while a < 10:
    a = a + 1
    
    if a == 7:
        continue
    print(a)

for i in range(2):
    for j in range(3):
        print(i, j)