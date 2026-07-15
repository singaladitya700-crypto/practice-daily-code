def count_vowels(text):
    text = text.lower()
    vowels = ["a","i","o","u","e"]
    total = 0
    con_total = 0
    for char in text:
        if char in vowels:
            total += 1
        else:
            if text.isalpha() == True:

                con_total += 1

    return total,con_total


print(count_vowels("ADITYATYF123"))
