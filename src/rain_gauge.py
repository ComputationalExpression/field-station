"""A rain gauge that totals the rain at the field station.

Author: TODO your name
"""


class RainGauge:
    """Keep the total rain, in millimeters, and how many readings made it."""

    def __init__(self, place):
        """Start a gauge at a place with no rain recorded."""
        self.place = place
        self.total = 0
        self.readings = 0

    def record(self, millimeters):
        """Add one reading to the total."""
        # TODO: Replace pass with two lines: add millimeters to self.total, and add 1 to self.readings
        pass

    def report(self):
        """Return one line about the rain so far."""
        return f"Rain at {self.place}: {self.total} mm over {self.readings} readings"


# Run this file by itself to try the class: uv run python src/rain_gauge.py
if __name__ == "__main__":
    gauge = RainGauge("the meadow")
    gauge.record(4)
    gauge.record(11)
    # Prints: Rain at the meadow: 15 mm over 2 readings
    print(gauge.report())
