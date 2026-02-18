# AC 2nd Accounts for High Score Tracker

import csv

accounts = []

file_path = "docs/accounts.csv"

def load_library():
    accounts.clear()

    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = {"Username": row["Username"], "Password": row["Password"], "Logged in Status": row["Logged in Status"]}
                accounts.append(account)

    except:
        print(f"\nFile '{file_path}' not found.")


def check_usernames(search_username):
    username_header = "Username"

    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Note: CSV data is read as strings, so search_value should also be a string
            if row[username_header] == search_username:
                return True
    return False

def check_password(username, password):
    pass
    
def login():
    typing_username = True

    while typing_username:
        username = input("\nEnter Username: ").strip()
        username_exist = check_usernames(username)

        if username_exist == False:
            while True:
                choice = input("\nUsername does not exist as an account.\n\n1. Enter Another Username\n\n2. Create an Account\n\nChoice: ").strip()

                if choice == "1":
                    break
                elif choice == "2":
                    # create account function
                    print("\nCreate account function calls here")
                    typing_username = False
                    break
                else:
                    print("\nPlease enter a valid choice (1 or 2)")

        elif username_exist:
            password = input("\nEnter Password: ")


               



load_library()
login()