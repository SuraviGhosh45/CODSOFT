def add_con(book):
    def add():
        while True:
            name = input("Enter Name: ")
            mob = input("Enter Mobile number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            # Add contact to the dictionary
            book[name] = {
                "mobile": mob,
                "email": email,
                "address": address
            }
            choice = input("Do you want to add another contact? (yes/no): ")
            if choice.lower().strip() != "yes":
                break

        print("Added Successfully!!")
    add()  # start adding contacts
def view_con(book):
    if not book:
        print("No contacts found.")
        return

    for name, details in book.items():
        print(f"Name: {name}")
        print(f"Mobile: {details['mobile']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}\n")


def search(book):
    choice = input("Search by name, mobile, or email: ").lower()
    found = False

    for name, details in book.items():
        if (choice == name.lower() or
                choice == details['mobile'].lower() or
                choice == details['email'].lower()):
            print(f"Name: {name}")
            print(f"Mobile: {details['mobile']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True
            break  # Stop searching

    if not found:
        print("Contact not found.")


def update_con(book):
    old = input("Enter the name of the contact to update: ").lower()
    if old in book:
        print("What do you want to change?")
        print("1. Name\n2. Mobile\n3. Email\n4. Address")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            new_name = input("Enter new name: ")
            book[new_name] = book.pop(old)
        elif choice == 2:
            new_num = input("Enter new mobile number: ")
            book[old]['mobile'] = new_num
        elif choice == 3:
            new_email = input("Enter new email: ")
            book[old]['email'] = new_email
        elif choice == 4:
            new_address = input("Enter new address: ")
            book[old]['address'] = new_address
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")
    print("Updated Successfully!")



def delete_con(book):
    name_to_delete = input("Enter the name of the contact to delete: ").lower()
    if name_to_delete in book:
        del book[name_to_delete]
        print("Deleted Successfully!")
    else:
        print("Contact not found!")


# Main function
contact_book = {}
while True:
    print("\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    select = int(input("Enter your choice (1/2/3/4/5/6): "))
    if select == 1:
       add_con(contact_book)
    elif select == 2:
       view_con(contact_book)
    elif select == 3:
        search(contact_book)
    elif select == 4:
        update_con(contact_book)
    elif select == 5:
        delete_con(contact_book)
    elif select == 6:
        print("Thank you for using this System!")
        break
    else:
        print("Wrong Input! Try again...")
