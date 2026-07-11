contacts = {
    "Aditya": "123431",
    "Rahul": "9876543210",
    "Aman": "9999999999"
    }
while True:
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


    choice = int(input("Enter your choice: "))

    cancel = ["done","cancel",]

    if choice == 1:
        name = input("enter a name :")

        if name in cancel:
            print("operation cancel")
        else:
            p_no = input("enter a number :")
            contacts[name] = p_no
            print("contact added successfully")

    elif choice == 2:
        name = input("enter a name :")
        p_no = contacts.get(name)
        if p_no is None:
            print("contact not found :")
        else:
            print(name , ":" , p_no)

    elif choice == 3:
        if len(contacts) == 0:
            print("no contact available")
        else:
            for k,v in contacts.items():
                print(k, ":" , v)

    elif choice == 4:
        name = input("enter a name :")
        unknown = contacts.get(name)
        if unknown is None:
            print("contact not found")
        else:
            p_no = input("enter a number :")
            contacts[name] = p_no
            print("contact updated")

    elif choice == 5:
        name = input("enter a name :")
        if name in contacts:
            del contacts[name]
            print("contact deleted")
        else:
            print("contact not found")
            
    elif choice == 6:
        print("Thank you for using contact book")
        break

print(contacts)