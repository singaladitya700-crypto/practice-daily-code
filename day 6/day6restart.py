# search_word = input("enter a word :")
# word_count = 0

# with open("test.txt" , "r") as file:
#     data = file.readlines()
   
# for line in data:
#     if search_word in line:
#         word_count += 1

# print(word_count)

# count = 1
# with open("data.txt" , "r") as file:
#     data = file.read()

# for ch in data:
#     if ch == "\n":
#         count += 1

# print(count)


frequency = {}

with open("data.txt" , "r") as file:
    data = file.read()
    words = data.split()

for word in words:
    word=word.lower()
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)