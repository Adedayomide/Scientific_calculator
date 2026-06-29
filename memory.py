"""
memory.py

Manages calculator memory operations.
"""


class MemoryManager:

    def __init__(self):

        self._memory = 0.0

    def store(self, value):
        """
        Store a value in memory.
        """

        self._memory = float(value)

    def recall(self):
        """
        Return the current memory value.
        """

        return self._memory

    def clear(self):
        """
        Clear memory.
        """

        self._memory = 0.0

    def add(self, value):
        """
        Add a value to memory.
        """

        self._memory += float(value)

    def subtract(self, value):
        """
        Subtract a value from memory.
        """

        self._memory -= float(value)

    def has_value(self):
        """
        Check if memory contains a non-zero value.
        """

        return self._memory != 0.0

    def get_display_value(self):
        """
        Return a user-friendly string.
        """

        if self._memory.is_integer():
            return str(int(self._memory))

        return str(self._memory)