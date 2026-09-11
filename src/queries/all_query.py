
"""SQLite query operations for the ``users`` table.

The methods in :class:`Query` receive an open SQLite connection, execute
parameterized statements, and return IDs, rows, or success flags.
"""

import sqlite3

class Query:
    """Namespace for database operations used by the service layer."""

    def __init__(self):
        pass

    @staticmethod
    def insert_user(connection, name, password):
        """Insert a user and return its generated ID, or ``None`` on conflict."""
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO users (name, password)
                VALUES (?, ?)
            """, (name, password))

            connection.commit()
            return cursor.lastrowid

        except sqlite3.IntegrityError:
            connection.rollback()
            print("این پسورد قبلاً ثبت شده است.")
            return None

    @staticmethod
    def get_user_by_name(connection, name):
        """Return the first ``(id, name, password)`` row matching ``name``."""
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, password FROM users WHERE name = ?", (name,))
        return cursor.fetchone()

    @staticmethod
    def get_all_users(connection):
        """Return all users as a list of ``(id, name, password)`` rows."""
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, password FROM users")
        return cursor.fetchall()


    def delete_user(connection, user_id):
        """Delete a user by ID and return whether a row was deleted."""
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        connection.commit()
        return cursor.rowcount > 0

    def update_user(connection, user_id, new_name):
        """Update a user's name and return whether a row was changed."""
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
        connection.commit()
        return cursor.rowcount > 0

    def get_user_by_id(connection, user_id):
        """Return the first ``(id, name, password)`` row matching ``user_id``."""
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, password FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

    def update_user_password(connection, user_id, new_password):
        """Update a user's password and return whether a row was changed."""
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        connection.commit()
        return cursor.rowcount > 0