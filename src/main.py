"""Activity 9: Field Station.

The field station at the Bousson Environmental Research Reserve keeps track of what happens on
its land. Each class is in its own file in src, and this file brings them together.

Author: TODO the names of everyone on your team
"""

from creek_gauge import CreekGauge
from feeder import Feeder
from rain_gauge import RainGauge
from trail_camera import TrailCamera


def make_station():
    """Make an object of each class, record something in it, and return the objects in a list."""
    station = []
    feeder = Feeder("the pond")
    feeder.visit(4)
    feeder.visit(2)
    gauge = RainGauge("the meadow")
    gauge.record(4)
    gauge.record(11)
    camera = TrailCamera("the creek trail")
    camera.photograph("deer")
    camera.photograph("heron")
    creek = CreekGauge("French Creek")
    creek.record(31)
    creek.record(52)
    creek.record(45)
    # TODO: Append feeder, gauge, camera and creek to station, in that order
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
