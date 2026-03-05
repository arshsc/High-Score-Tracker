# AC 2nd Accounts for High Score Tracker

import csv
from helper import *
from password import *
from pathlib import Path
current_file_path = Path(__file__).resolve()
current_dir = current_file_path.parent
parent_dir = current_dir.parent
target_file_path = parent_dir / "docs" / "accounts.csv"

accounts = []
accounts.clear()

try:
    with open(target_file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            account = {"Username": row["Username"], "Password": row["Password"], "Logged in Status": row["Logged in Status"]}
            accounts.append(account)

except:
    print(f"\nFile '{target_file_path}' not found.")


def check_usernames(search_username):
    username_header = "username"

    with open(target_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Note: CSV data is read as strings, so search_value should also be a string
            if row[username_header] == search_username:
                return True, {'username': row['username'], 'logged in': row['logged in']}
    return False, {}
    
def login():
    typing_username = True

    while typing_username:
        username = input("\nEnter Username: ").strip()
        username_exist = check_usernames(username)

        if username_exist == False:
            while True:
                choice = input("\nUsername does not exist as an account.\n\n1. Enter Another Username\n2. Create an Account\n\nChoice: ").strip()

                if choice == "1":
                    break
                elif choice == "2":
                    # create account function
                    typing_username = False
                    break
                else:
                    print("\nPlease enter a valid choice (1 or 2)")

        elif username_exist:
            for i in accounts:
                if i["username"] == username:
                    password = input("\nEnter Password: ")
                    password_match = pass_checker(password, i["password"])

            if password_match:
                print("True")
            elif not password_match:
                print("False")