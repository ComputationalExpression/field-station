"""A trail camera that keeps a list of the animals it photographs.

Author: TODO your name
"""


class TrailCamera:
    """Keep the animals a camera has photographed, in order."""

    def __init__(self, trail):
        """Start a camera on a trail with no photos."""
        self.trail = trail
        self.animals = []
        self.last = "none"

    def photograph(self, animal):
        """Add one animal to the photos, and keep it as the last one."""
        # TODO: Replace pass with two lines: append animal to self.animals, and store it as self.last
        pass

    def report(self):
        """Return one line about the photos so far."""
        return f"Camera on {self.trail}: {len(self.animals)} photos, the last a {self.last}"


# Run this file by itself to try the class: uv run python src/trail_camera.py
if __name__ == "__main__":
    camera = TrailCamera("the creek trail")
    camera.photograph("deer")
    camera.photograph("heron")
    # Prints: Camera on the creek trail: 2 photos, the last a heron
    print(camera.report())
