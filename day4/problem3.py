#method1

# text = input("enter worsds :")

# words = text.split()

# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1   

# print(frequency)

#method 2

text = input("enter worsds :")

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word,0) + 1

print(frequency)

"""
so how does method 2 works?
we take input

then we split that input in llist of words using split()

we need a new empty dictionary 

we use loop on list 

now the actual hard part begins 
frequency[word]= frequency.get(word,0) + 1 this iterates in loop for every word
for 1st word it will check if the word is in frequency or not if the word is in frequency then this is how it will look (word,1) + 1 = (word,2)
if the word is not present in frequency then it will become (word,1) thats how it work 
"""