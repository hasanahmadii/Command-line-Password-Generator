
"""Validate user names and generated password lengths before persistence."""


class Validation:
    """Provide the application's name and password validation rules."""

    def __init__(self):
        pass

    def check_validation_name(self, name):
        """Return ``True`` for alphabetic names shorter than ten characters."""
        if name.isalpha():
            if len(name) < 10 :
                return True
            else:
                return False
        return False

    def check_validation_pass(slef, lengh,password):
        """Return ``True`` when ``password`` has the requested length."""
        if len(password) == lengh:
            return True
        return False