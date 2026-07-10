#basics

list = [10 ,20 ,30 ,40 ,50]

print(list)
print(list[0])
print(list[4])
print(list[1:4])
list.append(60)
print(list)
list.insert(2,25)
print(list)
list.remove(40)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print(len(list))
print(min(list))
print(max(list))

for i in list:
    print(i)