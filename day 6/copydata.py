# with open ("data.txt" , "r") as file:
#     data = file.readlines()

# with open("backup.txt" , "w") as file:
#     for line in data:
#         file.write(line)


words = input("enter :")

with open("backup.txt", "a") as file:
    file.write("\n" + words)