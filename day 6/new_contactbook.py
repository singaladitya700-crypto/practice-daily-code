def load_contacts():
    contacts = {}

    with open("contacts.txt" , "r") as file:
        data = file.readlines()

    for line in data:
        line = line.strip()
        contact = line.split(":")

        contacts[contact[0]] = contact[1]

    return contacts

contacts = load_contacts()

def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, number in contacts.items():
            file.write(name + ":" + number + "\n")

            
cancel = ["done" , "back"]

def add_contact():
    name = input("enter a name :")

    if name in cancel:
        print("operation cancel")
    else:
        p_no = input("enter a number :")
        contacts[name] = p_no
        print("contact added successfully")

def search_contact():
    name = input("enter a name :")
    unknown = contacts.get(name)
    if unknown is None:
        print("contact not found")
    else:
        print(name,":",unknown)


def show_contacts():
    if len(contacts) == 0:
        print("No contacts available")
    else:
        for name, number in contacts.items():
            print(name, ":", number)

def update_contact():
    name = input("enter a name :")
    unknown = contacts.get(name)
    if unknown is None:
        print("contact not found")
    else:
        p_no = input("enter a number :")
        contacts[name] = p_no
        print("contact updated successfully")
    

def delete_contact():
    name = input("enter a name :")
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")
    

while True:

    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_contact()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        show_contacts()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        save_contacts()
        print("Thank you")
        break
    else:
        print("Invalid Choice")