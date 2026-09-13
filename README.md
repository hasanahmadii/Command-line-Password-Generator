# Command-line Password Generator

A simple Python-based command-line application for managing users and generating random passwords in a local SQLite database.

## Overview

This project allows you to:

- Create a user with a generated password
- Search for a user by name
- Update a user's name
- Update a user's password
- Delete a user
- List all users
- Automatically create the SQLite database and `users` table on first run

The app is built with Python and uses the SQLite database file `Userdatabase.db`.

## Important Security Notice

This project stores passwords in plain text in the SQLite database and displays them in some output paths. That is intentionally simple for learning/demo purposes only.

For real-world use, you should:

- Hash passwords using a secure algorithm such as bcrypt or Argon2
- Avoid printing raw passwords in logs or console output
- Use secret input handling for password entry
- Add authentication and authorization controls

## Requirements

- Python 3.10+
- `colorama`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Project Structure

```text
.
├── README.md
├── .gitignore
├── requirements.txt
├── .vscode/
│   └── settings.json
├── Userdatabase.db
└── src/
    ├── main.py
    ├── test.ipynb
    ├── database/
    │   └── concetion.py
    ├── logic/
    │   ├── generator.py
    │   ├── id_gen.py
    │   └── validation.py
    ├── queries/
    │   └── all_query.py
    └── services/
        └── user_service.py
```

## Running the Application

From the project root, run:

```bash
python -m src.main
```

On first run, the program creates the SQLite database and the `users` table automatically.

The menu offers the following choices:

1. Create user
2. Search user
3. Update user name
4. Update user password
5. Delete user
6. List all users
7. Exit

## Database Schema

The app creates a `users` table with the following structure:

| Column | Type | Description |
| --- | --- | --- |
| `id` | `INTEGER` | Auto-increment primary key |
| `name` | `TEXT` | User name |
| `password` | `TEXT` | Password value |

## Notes

- The database file is stored locally as `Userdatabase.db`.
- Password generation uses Python's `random` module and alphabet characters plus digits.
- The app is intended as a basic demonstration project rather than a production security system.

## License

This project does not currently include a license file. If you plan to publish or share it, consider adding an open-source license appropriate for your use case.
