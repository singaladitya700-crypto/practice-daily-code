def load_contacts():
    contacts = {}

    with open("contacts.txt" , "r") as file:
        contact = file.readlines()

    for line in contact:
        line = line.strip()
        parts = line.split(":")

        contacts[parts[0]] = parts[1]

    return contacts

contacts = load_contacts()
print(contacts)


def save_contacts():

    with open("contacts.txt" , "w")as file:
        for name , number in contacts.items():
            file.write(name + ":" + number + "\n")


contacts["aman"] = "098876"
save_contacts()