"""Command-line entry point for the password management application.

The module initializes the SQLite schema and repeatedly presents the user menu
until the user selects the exit option.
"""

from src.services.user_service import Controller
from src.logic.generator import Genrator
from src.database.concetion import DatabaseConnection
import sqlite3

def main():
    """Run one menu interaction and return whether the loop should continue."""
    c = Controller()
    user_input = input("Enter your choice (1-7): ")

    if user_input == "1":
        name = input("Enter user name: ")
        lenght = int(input("Enter password length: "))
        g1 = Genrator()
        password = g1.genrator_pass(lenght)  # Generate a random password of length lenght
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        c.create_user(connection,name, password)
        connection.close()
        return True  # Continue the loop after creating a user

    elif user_input == "2":
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        name = input("Enter user name to search: ")
        c.serach_user(connection, name)
        connection.close()
        return True  # Continue the loop after searching for a user


    elif user_input == "3":
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        user_id = int(input("Enter user ID to update name: "))
        new_name = input("Enter new name: ")
        c.update_user_name(connection, user_id, new_name)
        connection.close()
        return True  # Continue the loop after updating the name


    elif user_input == "4": 
        g1 = Genrator()
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        user_id = int(input("Enter user ID to update password: "))
        lenght = int(input("Enter new password length: "))
        new_password = g1.genrator_pass(lenght) 
        c.update_user_password(connection, user_id, new_password)
        connection.close()
        return True  # Continue the loop after updating the password


    elif user_input == "5":
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        user_id = int(input("Enter user ID to delete: "))
        c.delete_user(connection, user_id)
        connection.close()
        return True  # Continue the loop after deleting a user


    elif user_input == "6":
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        c.list_all_users(connection)
        connection.close()
        print("*"*90)
        return True  # Continue the loop after listing users


    elif user_input == "7":
        print("Exiting the program.")
        return False


if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.connect()  # Create the database and users table if they don't exist
    while True:
        if main():
            continue
        else:
            break
