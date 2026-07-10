numbers = [10,20,10,30,20,40]
no_dupli = []

for num in numbers:
    if num not in no_dupli:
        no_dupli.append(num)

print(no_dupli)