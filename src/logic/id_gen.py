"""Provide a simple in-memory incremental ID generator."""


class IdGen:
    """Generate sequential IDs for the lifetime of one instance."""

    def __init__(self):
        self.id = 0
        
    def generate_id(self):
        """Increment and return the next ID."""
        self.id += 1
        return self.id
