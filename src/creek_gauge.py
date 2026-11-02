"""A gauge that reads the level of a creek.

Author: TODO your name
"""


class CreekGauge:
    """Keep the levels of a creek and the highest one."""

    def __init__(self, creek):
        """Start a gauge on a creek with no readings."""
        self.creek = creek
        self.levels = []
        self.highest = 0

    def record(self, level):
        """Add one level to the readings, and keep it when it is the highest so far."""
        # TODO: Replace pass with: append level to self.levels, and when level is greater than
        # self.highest, store it as self.highest
        pass

    def report(self):
        """Return one line about the levels so far."""
        return f"{self.creek}: {len(self.levels)} readings, highest {self.highest}"


# Run this file by itself to try the class: uv run python src/creek_gauge.py
if __name__ == "__main__":
    creek = CreekGauge("French Creek")
    creek.record(31)
    creek.record(52)
    creek.record(45)
    # Prints: French Creek: 3 readings, highest 52
    print(creek.report())
