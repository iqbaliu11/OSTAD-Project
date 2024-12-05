import os
import csv

# File to store contact data
CONTACT_FILE = "contacts.csv"

def load_contacts():
    """Load contacts from the file into a dictionary."""
    contacts = {}
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, email, phone, address = row
                contacts[phone] = {"Name": name, "Email": email, "Address": address}
    return contacts

def save_contact(contact):
    """Save a single contact to the file."""
    with open(CONTACT_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow(contact)

def save_all_contacts(contacts):
    """Overwrite the file with all contacts."""
    with open(CONTACT_FILE, "w") as file:
        writer = csv.writer(file)
        for phone, details in contacts.items():
            writer.writerow([details["Name"], details["Email"], phone, details["Address"]])

def add_contact(contacts):
    """Allow the user to add a contact."""
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    if phone in contacts:
        print("Error: A contact with this phone number already exists.")
        return

    contacts[phone] = {"Name": name, "Email": email, "Address": address}
    save_contact([name, email, phone, address])
    print("Contact added successfully.")

def view_contacts(contacts):
    """Display all contacts in a user-friendly format."""
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts:")
        print("-" * 40)
        for phone, details in contacts.items():
            print(f"Name: {details['Name']}\nEmail: {details['Email']}\nPhone: {phone}\nAddress: {details['Address']}\n")
            print("-" * 40)

def remove_contact(contacts):
    """Delete a contact by phone number."""
    phone = input("Enter the phone number of the contact to remove: ").strip()
    if phone in contacts:
        del contacts[phone]
        save_all_contacts(contacts)
        print("Contact removed successfully.")
    else:
        print("Error: No contact found with this phone number.")

def search_contacts(contacts):
    """Search for a contact by name, email, or phone."""
    query = input("Enter search query: ").strip().lower()
    results = [details for phone, details in contacts.items() if query in phone or query in details["Name"].lower() or query in details["Email"].lower()]

    if results:
        print("\nSearch Results:")
        print("-" * 40)
        for result in results:
            print(f"Name: {result['Name']}\nEmail: {result['Email']}\nAddress: {result['Address']}\n")
            print("-" * 40)
    else:
        print("No contacts match your search.")

def main_menu():
    """Display the main menu and handle user choices."""
    contacts = load_contacts()

    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            search_contacts(contacts)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
