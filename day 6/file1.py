from pathlib import Path

file_path = Path(__file__).parent / "data.txt"

# file = open("data.txt" , "w")
# file.write("suprise ⚠️⚠️⚠️⚠️⚠️")
# file.close()

# with open ("data.txt" , "w") as file:
#     file.write("python\n")
#     file.write("file handling\n")
#     file.write("day6\n")


# with open("data.txt" , "r") as f:
#     file = f.readlines()

# print(len(file))


# search_word = input("enter a word :")

# with open(file_path, "r") as file:
#     data = file.read()

# words = data.split()

# if search_word in words:
#     print("word found")
# else:
#     print("word not found")


# count = 0
# search_word = input("enter a word :")

# with open(file_path, "r") as file:
#     data = file.read()

# words = data.split()

# for word in words:
#     if word == search_word:
#         count += 1

# print(f"{search_word} appears {count} times")
    


# count = 0
# search_word = input("enter a word :").lower()

with open(file_path , "r") as file:
    data = file.readlines()

print(data)

# for line in data:
#     if search_word in line.lower():
#         count += 1

# print(count)


# with open(file_path , "r") as file:
#     data = file.read()

# with open("backup.txt" , "w") as backup:
#     for line in data:
#         backup.write(line)
        
# note = input("enter a note :")
# with open(file_path , "a") as file:
#     file.write("\n" + note)

# count = 1
# with open(file_path , "r") as file:
#     data = file.read()

# for ch in data:
#     if ch == "\n":
#         count += 1          mm      [mp,]

# print(count)

# frequency = {}

# with open(file_path , "r") as file:
#     data = file.read()

# line = data.split()

# for word in line:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)


# def word_frequency(file_path):
#     frequency = {}
#     with open(file_path , "r") as file:
#         data = file.read()

#     line = data.split()

#     for word in line:
#         word = word.lower()
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1

#     return frequency

# print(word_frequency(file_path))