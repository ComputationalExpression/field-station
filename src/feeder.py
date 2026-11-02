"""A bird feeder at the field station.

Author: TODO your name
"""


class Feeder:
    """Count the birds that visit a feeder."""

    def __init__(self, place):
        """Start a feeder at a place with no visits."""
        self.place = place
        self.visits = 0

    def visit(self, birds):
        """Add a number of birds to the visits."""
        # TODO: Replace pass with a line that adds birds to self.visits
        pass

    def report(self):
        """Return one line about the visits so far."""
        return f"Feeder at {self.place}: {self.visits} birds"


# Run this file by itself to try the class: uv run python src/feeder.py
if __name__ == "__main__":
    feeder = Feeder("the pond")
    feeder.visit(4)
    feeder.visit(2)
    # Prints: Feeder at the pond: 6 birds
    print(feeder.report())
