"""Presentation services for the password management application.

`Controller` coordinates user input results with the query layer and prints
colorized success or failure messages.
"""

from colorama import Fore, Style


class Controller:
    """Display the menu and expose user-management operations."""
    def __init__(self):

        print(Fore.GREEN + "Welcome to the Password Management System!" + Style.RESET_ALL)
        print(Fore.YELLOW + "Please choose an option:" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Create a new user" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Search for a user" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Update name of a user" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Update password of a user" + Style.RESET_ALL)
        print(Fore.CYAN + "5. Delete a user" + Style.RESET_ALL)
        print(Fore.CYAN + "6. List all users" + Style.RESET_ALL)
        print(Fore.CYAN + "7. Exit" + Style.RESET_ALL)

    def create_user(self, connection, name, password):
        """Create a user and report the generated database ID."""
        from queries.all_query import Query
        user_id = Query.insert_user(connection, name, password)
        if user_id:
            print(Fore.GREEN + f"User created successfully with ID: {user_id}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to create user." + Style.RESET_ALL)

    def serach_user(self, connection, name):
        """Find a user by name and print the result."""
        from queries.all_query import Query
        user = Query.get_user_by_name(connection, name)
        if user:
            print(Fore.GREEN + f"User found: ID: {user[0]}, Name: {user[1]}, Password: {user[2]}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "User not found." + Style.RESET_ALL)

    def update_user_name(self, connection, user_id, new_name):
        """Update a user's name and report whether the operation succeeded."""
        from queries.all_query import Query
        success = Query.update_user(connection, user_id, new_name)
        if success:
            print(Fore.GREEN + "User name updated successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to update user name." + Style.RESET_ALL)

    def update_user_password(self, connection, user_id, new_password):
        """Update a user's password and report whether it succeeded."""
        from queries.all_query import Query
        success = Query.update_user_password(connection, user_id, new_password)
        if success:
            print(Fore.GREEN + "User password updated successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to update user password." + Style.RESET_ALL)

    def delete_user(self, connection, user_id):
        """Delete a user by ID and report whether the operation succeeded."""
        from queries.all_query import Query
        success = Query.delete_user(connection, user_id)
        if success:
            print(Fore.GREEN + "User deleted successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to delete user." + Style.RESET_ALL)

    def list_all_users(self, connection):
        """Print every user currently stored in the database."""
        from queries.all_query import Query
        users = Query.get_all_users(connection)
        if users:
            print(Fore.GREEN + "List of all users:" + Style.RESET_ALL)
            for user in users:
                print(Fore.CYAN + f"ID: {user[0]}, Name: {user[1]}, Password: {user[2]}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "No users found." + Style.RESET_ALL)
        
        