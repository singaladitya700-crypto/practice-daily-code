# word = input("enter a word :")

# frequency = {}

# for ch in word:
#     if ch in frequency:
#         frequency[ch] += 1
#     else:
#         frequency[ch] = 1

# print(frequency)


#method 2

word = input("enter a word :")

frequency = {}

for ch in word:
    frequency[ch] = frequency.get(ch,0) + 1

print(frequency)