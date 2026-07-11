#phone book

phone_book = {
    "Aditya": "9876543210",
    "Rahul": "9123456789",
    "Aman": "9988776655"
}

name = input("enter a name :")
number = phone_book.get(name)

if number is None:
    print("Contact not found")
else:
    print(name,":",number)