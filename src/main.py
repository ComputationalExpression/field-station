"""Activity 9: Field Station.

The field station at the Bousson Environmental Research Reserve keeps track of what happens on
its land. Each teammate writes a class for one thing the station tracks, in a separate file in
src. This file brings those classes together.

Author: TODO the names of everyone on your team
"""

# TODO: Import each teammate's class, one line per file, such as: from feeder import Feeder


def make_station():
    """Make an object of each teammate's class and return the objects in a list."""
    station = []
    # TODO: For each class, make an object, call a method that records something in it,
    # and append the object to station.
    return station


def main():
    """Print the report of every object at the station."""
    print("=" * 50)
    print("BOUSSON FIELD STATION")
    print("=" * 50)
    for thing in make_station():
        print(thing.report())


if __name__ == "__main__":
    main()
