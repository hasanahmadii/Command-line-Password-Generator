"""Create and initialize the application's SQLite database."""
import sqlite3


class DatabaseConnection:
    """Ensure the local database and its ``users`` table exist."""

    def __init__(self):
        pass

    def connect(self):
        """Create the schema if needed, then close the initialization connection."""
        # نام فایل دیتابیس
        import sqlite3
        # نام فایل دیتابیس
        DATABASE_NAME = "Userdatabase.db"
        # اتصال به دیتابیس
        connection = sqlite3.connect(DATABASE_NAME)
        # ساخت جدول در صورت نبودن
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL UNIQUE
            )
        """)
        # ذخیره تغییرات
        connection.commit()
        # بستن اتصال
        connection.close()
        print("Database and users table are ready.")
