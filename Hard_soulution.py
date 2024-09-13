import os
import time

# Create a function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class User:
    def __init__(self, first_name, last_name, ID, status=""):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.status = status

# Ask the user to input the data
def create_user():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    ID = input("Enter your ID: ")
    status = input("Enter the status: ") or "press enter to continue....."
    return User(first_name, last_name, ID, status)

# Display user information
def display_user(user):
    print(f"First Name: {user.first_name}")
    print(f"Last Name: {user.last_name}")
    print(f"ID: {user.ID}")
    print(f"Status: {user.status}")
    print("_" * 20)

# Search for a member by using a function
def search_member(members):
    clear_screen()
    print("Search by using:")
    print("1. Membership ID")
    print("2. First Name")
    print("3. Membership Status")
    search_choice = input("Enter your choice: ")
    found_members = []

    if search_choice == "1":
        search_id = input("Enter the Membership ID: ")
        found_members = [member for member in members if member.ID == search_id]
    elif search_choice == "2":
        search_name = input("Enter the First Name: ").lower()
        found_members = [member for member in members if member.first_name.lower() == search_name]
    elif search_choice == "3":
        search_status = input("Enter the Membership Status: ").lower()
        found_members = [member for member in members if member.status.lower() == search_status]

    if found_members:
        print("\nFound Members:")
        for member in found_members:
            display_user(member)
    else:
        print("No members found matching the search criteria.")

# Create a list to store members
Members = []

while True:
    clear_screen()
    print("Welcome to Gym Membership Management:\n")
    print("Choose an action:")
    print("1. Add a new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit")
    
    # Ask the user about their choice
    choice = input("Enter your choice: ")

    if choice == "1":
        Members.append(create_user())
        print("Member added successfully!")
        time.sleep(2)
    
    elif choice == "2":
        clear_screen()
        if Members:
            print("Displaying all members...")
            for member in Members:
                display_user(member)
                time.sleep(2)
        else:
            print("No members to display!")
        time.sleep(2)

    elif choice == "3":
        search_member(Members)
        time.sleep(2)

    elif choice == "4":
        break

    else:
        print("Invalid choice, please try again.")
        time.sleep(2)
