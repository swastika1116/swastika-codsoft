# Contact Book Code in Python

# Initialize an empty dictionary to store contacts
contact_book = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contact_book:
        print("Contact book is empty!")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contact_book:
        print(f"Name: {name}, Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("you've exited :)")
        break
    else:
        print("Invalid choice. Please try again!")
