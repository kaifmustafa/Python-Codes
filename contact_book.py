def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def contact_book():
    contacts = {}
    while True:
        print("\nContact Book")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting contact book!")
            break
        else:
            print("Invalid input! Please choose between 1-4.")

# Run the contact book
if __name__ == "__main__":
    contact_book()