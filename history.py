"""
history.py

Stores and manages calculator history.
"""

from settings import MAX_HISTORY_ITEMS


class HistoryManager:

    def __init__(self):

        self._history = []

    def add(self, expression, result):
        """
        Add a new calculation to history.
        """

        entry = {
            "expression": str(expression),
            "result": str(result)
        }

        self._history.append(entry)

        if len(self._history) > MAX_HISTORY_ITEMS:
            self._history.pop(0)

    def get_all(self):
        """
        Return all history entries.
        """

        return self._history.copy()

    def get_last(self):
        """
        Return the latest history entry.
        """

        if not self._history:
            return None

        return self._history[-1]

    def clear(self):
        """
        Remove all history entries.
        """

        self._history.clear()

    def remove(self, index):
        """
        Remove a history entry by index.
        """

        if 0 <= index < len(self._history):
            self._history.pop(index)

    def count(self):
        """
        Return number of stored calculations.
        """

        return len(self._history)

    def is_empty(self):
        """
        Check whether history is empty.
        """

        return len(self._history) == 0

    def export(self):
        """
        Export history as formatted text.
        """

        lines = []

        for item in self._history:

            lines.append(
                f"{item['expression']} = {item['result']}"
            )

        return "\n".join(lines)