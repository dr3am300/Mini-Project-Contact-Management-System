# Project Requirements
# Your task is to develop a Contact Management System with the following features:

# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:

# Welcome to the Contact Management System! 
#  Menu:
# 1. Add a new contact
# 2. Edit an existing contact
# 3. Delete a contact
# 4. Search for a contact
# 5. Display all contacts
# 6. Export contacts to a text file
# 7. Import contacts from a text file *BONUS*
# 8. Quit

# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.

# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).

# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact.
# Searching for a contact and displaying their details.
# Displaying a list of all contacts.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system. * BONUS

# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
# Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.


welcome_message = "Welcome to the Contact Management System!"
start_up_message = "Starting up the Contact Management System..."
print(start_up_message)
do_you = input("Do you want to continue? (YES/NO): ").upper()
if do_you == "YES":
    print(welcome_message)
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Contact Management System is ready!")
else:
    print("Quitting the Contact Management System...")
    count = 10
    while count > 0:
        print(count)
        count -= 1
    exit()
    

menu = """
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Create a new text file 
7. Write in existing text file contact information
8. Edit contact information in existing text file
9. List all contact information in existing text file
10. Export contact information to a existing text file
11. Import contact information from a text file
12. Quit
"""


def add_contact():
    print("Adding a new contact...")
    would_you = input("Would you like to add a new contact? (YES/NO): ").upper()
    if would_you == "YES":
        name = input("Enter the contact's name: ")
        import re
        def name_validation(name):
            name_pattern = re.compile(r"^[a-zA-Z ]+$")
            return name_pattern.match(name)
        if name_validation(name):
            print("Valid name!")
        else:
            print("Invalid name! Please enter a valid name.")
            name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        import re
        def phone_number_validation(phone_number):
            phone_number_pattern = re.compile(r"^\d{10}$")
            return phone_number_pattern.match(phone_number)
        if phone_number_validation(phone_number):
            print("Valid phone number!")
        else:
            print("Invalid phone number! Please enter a 10-digit phone number.")
            phone_number = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        import re
        def email_validation(email):
            email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
            return email_pattern.match(email)
        if email_validation(email):
            print("Valid email address!")
        else:
            print("Invalid email address! Please enter a valid email address.")
            email = input("Enter the contact's email address: ")
        additional_info = input("Enter any additional information: ")
        contact = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "additional_info": additional_info
        }
        contacts[phone_number] = contact
        print("Contact added successfully!")  
    elif would_you == "NO":
        print("Returning to the main menu...")
        return menu
    else:
        print("Invalid choice! Please try again.")
        return
    would_you = input("Would you like to continue adding another contact? (YES/NO): ").upper()
    if would_you == "YES":
        add_contact()
    else:
        print("Returning to the main menu...")
        return menu
def edit_contact():
    print("Editing an existing contact...")
    would_you = input("Would you like to search for the contact first? (YES/NO): ").upper()
    if would_you == "YES":
        would_you = input(" Select the option you would like to search by: \n 1. Phone number \n 2. Name \n 3. Email \n enter the number: ")
        if would_you == "1":
            phone_number = input("Enter the contact's phone number: ")
            import re
            def phone_number_validation(phone_number):
                phone_number_pattern = re.compile(r"^\d{10}$")
                return phone_number_pattern.match(phone_number)
            if phone_number_validation(phone_number):
                print("Valid phone number!")
                would_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
                if would_you == "YES":
                    phone_number = input("Enter the contact's phone number: ")
                    import re
                    def phone_number_validation(phone_number):
                        phone_number_pattern = re.compile(r"^\d{10}$")
                        return phone_number_pattern.match(phone_number)
                    if phone_number_validation(phone_number):
                        print("Valid phone number!")
                    else:
                        print("Invalid phone number! Please enter a 10-digit phone number.")
                        phone_number = input("Enter the contact's phone number: ")
                if would_you == "NO":
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Invalid phone number! Please enter a 10-digit phone number.")
                phone_number = input("Enter the contact's phone number: ")
            if phone_number in contacts:
                contact = contacts[phone_number]
                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone number:", contact["phone_number"])
                print("Email:", contact["email"])
                print("Additional information:", contact["additional_info"])
            else:
                print("Contact not found!")
                return
        elif would_you == "2":
            name = input("Enter the contact's name: ")
            import re
            def name_validation(name):
                name_pattern = re.compile(r"^[a-zA-Z ]+$")
                return name_pattern.match(name)
            if name_validation(name):
                print("Valid name!")
                would_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
                if would_you == "YES":
                    name = input("Enter the contact's name: ")
                    import re
                    def name_validation(name):
                        name_pattern = re.compile(r"^[a-zA-Z ]+$")
                        return name_pattern.match(name)
                    if name_validation(name):
                        print("Valid name!")
                    else:
                        print("Invalid name! Please enter a valid name.")
                        name = input("Enter the contact's name: ")
                if would_you == "NO":
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Invalid name! Please enter a valid name.")
                name = input("Enter the contact's name: ")
            for phone_number, contact in contacts.items():
                if contact["name"] == name:
                    print("Contact found!")
                    print("Name:", contact["name"])
                    print("Phone number:", contact["phone_number"])
                    print("Email:", contact["email"])
                    print("Additional information:", contact["additional_info"])
                    break
            else:
                print("Contact not found!")
                return
        elif would_you == "3":
            email = input("Enter the contact's email address: ")
            import re
            def email_validation(email):
                email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                return email_pattern.match(email)
            if email_validation(email):
                print("Valid email address!")
                would_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
                if would_you == "YES":
                    email = input("Enter the contact's email address: ")
                    import re
                    def email_validation(email):
                        email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                        return email_pattern.match(email)
                    if email_validation(email):
                        print("Valid email address!")
                    else:
                        print("Invalid email address! Please enter a valid email address.")
                        email = input("Enter the contact's email address: ")
                if would_you == "NO":
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Invalid email address! Please enter a valid email address.")
                email = input("Enter the contact's email address: ")
            for phone_number, contact in contacts.items():
                if contact["email"] == email:
                    print("Contact found!")
                    print("Name:", contact["name"])
                    print("Phone number:", contact["phone_number"])
                    print("Email:", contact["email"])
                    print("Additional information:", contact["additional_info"])
                    break
            else:
                print("Contact not found!")
                return
    elif would_you == "NO":
        input_any = input("Enter any information you have about the contact: ")
        for phone_number, name, email, additional_info in contacts.items():
            if input_any in contacts:
                contact = contacts[input_any]
                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone number:", contact["phone_number"])
                print("Email:", contact["email"])
                print("Additional information:", contact["additional_info"])
                would_you = input("Are you sure you want to edit this contact? (YES/NO): ").upper()
                if would_you == "YES":
                    name = input("Enter the contact's name: ")
                    import re
                    def name_validation(name):
                        name_pattern = re.compile(r"^[a-zA-Z ]+$")
                        return name_pattern.match(name)
                    if name_validation(name):
                        print("Valid name!")
                    else:
                        print("Invalid name! Please enter a valid name.")
                        name = input("Enter the contact's name: ")
                    phone_number = input("Enter the contact's phone number: ")
                    import re
                    def phone_number_validation(phone_number):
                        phone_number_pattern = re.compile(r"^\d{10}$")
                        return phone_number_pattern.match(phone_number)
                    if phone_number_validation(phone_number):
                        print("Valid phone number!")
                    else:
                        print("Invalid phone number! Please enter a 10-digit phone number.")
                        phone_number = input("Enter the contact's phone number: ")
                    email = input("Enter the contact's email address: ")
                    import re
                    def email_validation(email):
                        email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                        return email_pattern.match(email)
                    if email_validation(email):
                        print("Valid email address!")
                    else:
                        print("Invalid email address! Please enter a valid email address.")
                        email = input("Enter the contact's email address: ")
                    additional_info = input("Enter any additional information: ")
                    contact = {
                        "name": name,
                        "phone_number": phone_number,
                        "email": email,
                        "additional_info": additional_info
                    }
                    contacts[phone_number] = contact
                    print("Contact edited successfully!")
                else:
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Contact not found!")
                return
    else:
        print("Invalid choice! Please try again.")
        return
    would_you = input("Would you like to continue editing another contact? (YES/NO): ").upper()
    if would_you == "YES":
        edit_contact()
    else:
        print("Returning to the main menu...")
        return menu              
def delete_contact():
    print("Deleting a contact...")
    do_you = input("Would you like to search for the contact first? (YES/NO): ").upper()
    if do_you == "YES":
        do_you = input(" Select the option you would like to search by: \n 1. Phone number \n 2. Name \n 3. Email \n enter the number: ")
        if do_you == "1":
            phone_number = input("Enter the contact's phone number: ")
            import re
            def phone_number_validation(phone_number):
                phone_number_pattern = re.compile(r"^\d{10}$")
                return phone_number_pattern.match(phone_number)
            if phone_number_validation(phone_number):
                print("Valid phone number!")
                do_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
                if do_you == "YES":
                    phone_number = input("Enter the contact's phone number: ")
                    import re
                    def phone_number_validation(phone_number):
                        phone_number_pattern = re.compile(r"^\d{10}$")
                        return phone_number_pattern.match(phone_number)
                    if phone_number_validation(phone_number):
                        print("Valid phone number!")
                    else:
                        print("Invalid phone number! Please enter a 10-digit phone number.")
                        phone_number = input("Enter the contact's phone number: ")
                if do_you == "NO":
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Invalid phone number! Please enter a 10-digit phone number.")
                phone_number = input("Enter the contact's phone number: ")
            if phone_number in contacts:
                contact = contacts[phone_number]
                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone number:", contact["phone_number"])
                print("Email:", contact["email"])
                print("Additional information:", contact["additional_info"])
                do_you = input("Are you sure you want to delete this contact? (YES/NO): ").upper()
                if do_you == "YES":
                    del contacts[phone_number]
                    print("Contact deleted successfully!")
                else:
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Contact not found!")
                return
        elif do_you == "2":
            name = input("Enter the contact's name: ")
            import re
            def name_validation(name):
                name_pattern = re.compile(r"^[a-zA-Z ]+$")
                return name_pattern.match(name)
            if name_validation(name):
                print("Valid name!")
                do_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
                if do_you == "YES":
                    name = input("Enter the contact's name: ")
                    import re
                    def name_validation(name):
                        name_pattern = re.compile(r"^[a-zA-Z ]+$")
                        return name_pattern.match(name)
                    if name_validation(name):
                        print("Valid name!")
                    else:
                        print("Invalid name! Please enter a valid name.")
                        name = input("Enter the contact's name: ")
                if do_you == "NO":
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Invalid name! Please enter a valid name.")
                name = input("Enter the contact's name: ")
            for phone_number, contact in contacts.items():
                if contact["name"] == name:
                    print("Contact found!")
                    print("Name:", contact["name"])
                    print("Phone number:", contact["phone_number"])
                    print("Email:", contact["email"])
                    print("Additional information:", contact["additional_info"])
                    do_you = input("Are you sure you want to delete this contact? (YES/NO): ").upper()
                    if do_you == "YES":
                        del contacts[phone_number]
                        print("Contact deleted successfully!")
                    else:
                        print("Returning to the main menu...")
                        return menu
                    break
            else:
                print("Contact not found!")
                return
        elif do_you == "3":
            email = input("Enter the contact's email address: ")
            import re
            def email_validation(email):
                email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                return email_pattern.match(email)
            if email_validation(email):
                print("Valid email address!")
                do_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
                if do_you == "YES":
                    email = input("Enter the contact's email address: ")
                    import re
                    def email_validation(email):
                        email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                        return email_pattern.match(email)
                    if email_validation(email):
                        print("Valid email address!")
                    else:
                        print("Invalid email address! Please enter a valid email address.")
                        email = input("Enter the contact's email address: ")
                if do_you == "NO":
                    print("Returning to the main menu...")
                    return menu
            else:
                print("Invalid email address! Please enter a valid email address.")
                email = input("Enter the contact's email address: ")
            for phone_number, contact in contacts.items():
                if contact["email"] == email:
                    print("Contact found!")
                    print("Name:", contact["name"])
                    print("Phone number:", contact["phone_number"])
                    print("Email:", contact["email"])
                    print("Additional information:", contact["additional_info"])
                    do_you = input("Are you sure you want to delete this contact? (YES/NO): ").upper()
                    if do_you == "YES":
                        del contacts[phone_number]
                        print("Contact deleted successfully!")
                    else:
                        print("Returning to the main menu...")
                        return menu
                    break
            else:
                print("Contact not found!")
                return
    elif do_you == "NO":
        phone_number = input("Enter the contact's phone number: ")
        import re
        def phone_number_validation(phone_number):
            phone_number_pattern = re.compile(r"^\d{10}$")
            return phone_number_pattern.match(phone_number)
        if phone_number_validation(phone_number):
            print("Valid phone number!")
        else:
            print("Invalid phone number! Please enter a 10-digit phone number.")
            phone_number = input("Enter the contact's phone number: ")
        if phone_number in contacts:
            contact = contacts[phone_number]
            print("Contact found!")
            print("Name:", contact["name"])
            print("Phone number:", contact["phone_number"])
            print("Email:", contact["email"])
            print("Additional information:", contact["additional_info"])
            do_you = input("Are you sure you want to delete this contact? (YES/NO): ").upper()
            if do_you == "YES":
                del contacts[phone_number]
                print("Contact deleted successfully!")
            else:
                print("Returning to the main menu...")
                return menu
        else:
            print("Contact not found!")
            return
    else:
        print("Invalid choice! Please try again.")
        return
    would_you = input("Would you like to continue deleting another contact? (YES/NO): ").upper()
    if would_you == "YES":
        delete_contact()
    else:
        print("Returning to the main menu...")
        return menu
    
import os
contacts = {}        
def search_contact():
    print("Searching for a contact...")
    to_do = input(" Select the option you would like to search by: \n 1. Phone number \n 2. Name \n 3. Email \n enter the number: ")
    if to_do == "1":
        phone_number = input("Enter the contact's phone number: ")
        import re
        def phone_number_validation(phone_number):
            phone_number_pattern = re.compile(r"^\d{10}$")
            return phone_number_pattern.match(phone_number)
        if phone_number_validation(phone_number):
            print("Valid phone number!")
            would_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
            if would_you == "YES":
                phone_number = input("Enter the contact's phone number: ")
                import re
                def phone_number_validation(phone_number):
                    phone_number_pattern = re.compile(r"^\d{10}$")
                    return phone_number_pattern.match(phone_number)
                if phone_number_validation(phone_number):
                    print("Valid phone number!")
                else:
                    print("Invalid phone number! Please enter a 10-digit phone number.")
                    phone_number = input("Enter the contact's phone number: ")
            if would_you == "NO":
                print("Returning to the main menu...")
                return menu
        else:
            print("Invalid phone number! Please enter a 10-digit phone number.")
            phone_number = input("Enter the contact's phone number: ")
        if phone_number in contacts:
            contact = contacts[phone_number]
            print("Contact found!")
            print("Name:", contact["name"])
            print("Phone number:", contact["phone_number"])
            print("Email:", contact["email"])
            print("Additional information:", contact["additional_info"])
        else:
            print("Contact not found!")
            return
    elif to_do == "2":
        name = input("Enter the contact's name: ")
        import re
        def name_validation(name):
            name_pattern = re.compile(r"^[a-zA-Z ]+$")
            return name_pattern.match(name)
        if name_validation(name):
            print("Valid name!")
            would_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
            if would_you == "YES":
                name = input("Enter the contact's name: ")
                import re
                def name_validation(name):
                    name_pattern = re.compile(r"^[a-zA-Z ]+$")
                    return name_pattern.match(name)
                if name_validation(name):
                    print("Valid name!")
                else:
                    print("Invalid name! Please enter a valid name.")
                    name = input("Enter the contact's name: ")
            if would_you == "NO":
                print("Returning to the main menu...")
                return menu
        else:
            print("Invalid name! Please enter a valid name.")
            name = input("Enter the contact's name: ")
        for phone_number, contact in contacts.items():
            if contact["name"] == name:
                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone number:", contact["phone_number"])
                print("Email:", contact["email"])
                print("Additional information:", contact["additional_info"])
                break
        else:
            print("Contact not found!")
            return
    elif to_do == "3":
        email = input("Enter the contact's email address: ")
        import re
        def email_validation(email):
            email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
            return email_pattern.match(email)
        if email_validation(email):
            print("Valid email address!")
            would_you = input(" Would you like to continue or search by another option? (YES/NO): ").upper()
            if would_you == "YES":
                email = input("Enter the contact's email address: ")
                import re
                def email_validation(email):
                    email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                    return email_pattern.match(email)
                if email_validation(email):
                    print("Valid email address!")
                else:
                    print("Invalid email address! Please enter a valid email address.")
                    email = input("Enter the contact's email address: ")
            if would_you == "NO":
                print("Returning to the main menu...")
                return menu
        else:
            print("Invalid email address! Please enter a valid email address.")
            email = input("Enter the contact's email address: ")
        for phone_number, contact in contacts.items():
            if contact["email"] == email:
                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone number:", contact["phone_number"])
                print("Email:", contact["email"])
                print("Additional information:", contact["additional_info"])
                break
        else:
            print("Contact not found!")
            return
    else:
        print("Invalid choice! Please try again.")
        return
    would_you = input("Would you like to continue searching for another contact? (YES/NO): ").upper()
    if would_you == "YES":
        search_contact()
    else:
        print("Returning to the main menu...")
        return menu   
def display_contacts():
    print("Displaying all contacts...")
    would_you = input("Would you like to display all contacts? (YES/NO): ").upper()
    if would_you == "YES":
        for phone_number, contact in contacts.items():
            print("Phone number:", phone_number)
            print("Name:", contact["name"])
            print("Phone number:", contact["phone_number"])
            print("Email:", contact["email"])
            print("Additional information:", contact["additional_info"])
            print()
    elif would_you == "NO":
        print("Returning to the main menu...")
        return menu
    else:
        print("Invalid choice! Please try again.")
        return
    would_you = input("Would you like to continue displaying all contacts? (YES/NO): ").upper()
    if would_you == "YES":
        display_contacts()
    else:
        print("Returning to the main menu...")
        return menu
    

def create_text_file():
    print("Creating a new text file...")
    file_name = input("Enter the name of the text file: ")
    with open(file_name, "w") as file:
        print("Text file created successfully!")
        
def write_in_text_file():
    print("Writing in an existing text file...")
    file_name = input("Enter the name of the text file: ")
    if file_name not in os.listdir():
        print("File not found!")
        return
    with open(file_name, "a") as file:
        contact_name = input("Enter the contact's name: ")
        import re
        def name_validation(name):
            name_pattern = re.compile(r"^[a-zA-Z ]+$")
            return name_pattern.match(name)
        if name_validation(contact_name):
            print("Valid name!")
        else:
            print("Invalid name! Please enter a valid name.")
            contact_name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        import re
        def phone_number_validation(phone_number):
            phone_number_pattern = re.compile(r"^\d{10}$")
            return phone_number_pattern.match(phone_number)
        if phone_number_validation(phone_number):
            print("Valid phone number!")
        else:
            print("Invalid phone number! Please enter a 10-digit phone number.")
            phone_number = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        import re
        def email_validation(email):
            email_pattern = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
            return email_pattern.match(email)
        if email_validation(email):
            print("Valid email address!")
        else:
            print("Invalid email address! Please enter a valid email address.")
            email = input("Enter the contact's email address: ")
        additional_info = input("Enter any additional information: ")
        file.write(f"Name: {contact_name}\n")
        file.write(f"Phone number: {phone_number}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Additional information: {additional_info}\n")
        file.write("\n")
        print("Contact information written to the text file successfully!")
        
def edit_text_file():
    print("Editing contact information in an existing text file...")
    file_name = input("Enter the name of the text file: ")
    if file_name not in os.listdir():
        print("File not found!")
        return
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        contact_name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        additional_info = input("Enter any additional information: ")
        for line in lines:
            if "Name:" in line:
                file.write(f"Name: {contact_name}\n")
            elif "Phone number:" in line:
                file.write(f"Phone number: {phone_number}\n")
            elif "Email:" in line:
                file.write(f"Email: {email}\n")
            elif "Additional information:" in line:
                file.write(f"Additional information: {additional_info}\n")
            else:
                file.write(line)
        print("Contact information edited in the text file successfully!")
        
def list_text_file():
    print("Listing all contact information in an existing text file...")
    file_name = input("Enter the name of the text file: ")
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")
            
def export_to_text_file():
    print("Exporting contact information to an existing text file...")
    file_name = input("Enter the name of the text file: ")
    if file_name not in os.listdir():
        print("File not found!")
        return
    with open(file_name, "w") as file:
        for phone_number, contact in contacts.items():
            file.write(f"Phone number: {phone_number}\n")
            file.write(f"Name: {contact['name']}\n")
            file.write(f"Phone number: {contact['phone_number']}\n")
            file.write(f"Email: {contact['email']}\n")
            file.write(f"Additional information: {contact['additional_info']}\n")
            file.write("\n")
        print("Contact information exported to the text file successfully!")
        
def import_from_text_file():
    print("Importing contact information from a text file...")
    file_name = input("Enter the name of the text file: ")
    if file_name not in os.listdir():
        print("File not found!")
        return
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            phone_number = lines[i].strip().split(": ")[1]
            name = lines[i + 1].strip().split(": ")[1]
            phone_number = lines[i + 2].strip().split(": ")[1]
            email = lines[i + 3].strip().split(": ")[1]
            additional_info = lines[i + 4].strip().split(": ")[1]
            contact = {
                "name": name,
                "phone_number": phone_number,
                "email": email,
                "additional_info": additional_info
            }
            contacts[phone_number] = contact
        print("Contact information imported from the text file successfully!")
        

def quit():
    print(" Are you sure you want to quit?")
    do_you = input("YES/NO: ").upper()
    if do_you == "YES":
        print("Quitting the Contact Management System...")
        count = 10
        while count > 0:
            print(count)
            count -= 1
        exit()
    else:
        print("Returning to the main menu...")
        return menu
    


if __name__ == "__main__":
    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            create_text_file()
        elif choice == "7":
            write_in_text_file()
        elif choice == "8":
            edit_text_file()
        elif choice == "9":
            list_text_file()
        elif choice == "10":
            export_to_text_file()
        elif choice == "11":
            import_from_text_file()
        elif choice == "12":
            quit()
        else:
            print("Invalid choice! Please try again.")
            continue
        print()
        