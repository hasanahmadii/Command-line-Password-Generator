
"""Generate random passwords from ASCII letters and digits."""
import random
import string

class Genrator:
    """Generate passwords using the character set configured at initialization."""

    def __init__(self):
        self.data = (string.ascii_letters+string.digits)

    def genrator_pass(self, lenght):
        """Return a random password containing exactly ``lenght`` characters."""
        
        return "".join(random.choices(self.data,k=lenght))