def add_contact():
    #Adds a new contact to the contact book.
    name = input("Enter contact's name: ")
    phone = input("Enter contact's phone number: ")
    email = input("Enter contact's email (optional): ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")
 
 
def view_contacts():
    #Displays all contacts in the contact book.
    if not contacts:
        print("Contact book is empty.")
        return
    for name, info in contacts.items():
        print(
            f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email'] or 'N/A'}\n"
            + "-" * 20
        )
 
 
def search_contact():
    #Searches for a contact by name.
    name = input("Enter the contact's name to search for: ")
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email'] or 'N/A'}")
    else:
        print(f"Contact '{name}' not found.")
 
 
def delete_contact():
    #Deletes a contact from the contact book.
    name = input("Enter the contact's name to delete: ")
    if contacts.pop(name, None):
        print(f"Contact '{name}' deleted!")
    else:
        print(f"Contact '{name}' not found.")
 
 
# Initialize an empty dictionary to store contacts
contacts = {
    "Thato Ndlovu": {"phone": "+273-456-7890", "email": "NdlovuT.Student@outlook.com"},
    "Raphaahle Mogano": {"phone": "+274-567-8901", "email": "MoganoR.Student@outlook.com"},
    "Teddy Motswiri": {"phone": "+275-678-9012", "email": "MotswiriT.Student@outlook.com"},
    "Matome Ramatsoma": {"phone": "+273-456-7890", "email": "RamatsomaM.Student@outlook.com"},
    "Bongane Ntombela": {"phone": "+273-456-7890", "email": "NtombelaB.Student@outlook.com"},
}
 
# Main program loop
while True:
    print(
        "\nContact Book Menu:\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit"
    )
    choice = input("Enter your choice: ")
    if choice in ("1", "2", "3", "4"):
        eval(
            f"{['add_contact', 'view_contacts', 'search_contact', 'delete_contact'][int(choice)-1]}()"
        )
    elif choice == "5":
        break
    else:
        print("Invalid choice.")