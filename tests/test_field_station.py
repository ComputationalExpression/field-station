"""Checks for Activity 9: Field Station.

Each class has a check of its own, which makes an object, calls its recording
method, and reads its attributes, so a teammate's check passes on their own
file whatever state the others are in. The git checks read the repository's
history: the merges GitHub makes for pull requests, and who committed to src.
"""

import subprocess
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"


def git(*args):
    """Run a git command in the repository and return its output."""
    result = subprocess.run(
        ["git", *args], cwd=SRC.parent, capture_output=True, text=True, check=False
    )
    return result.stdout


def test_feeder_counts_visits():
    from feeder import Feeder

    feeder = Feeder("the pond")
    feeder.visit(4)
    feeder.visit(2)
    assert feeder.visits == 6, (
        f"after visit(4) and visit(2), visits was {feeder.visits}, expected 6: add birds to self.visits"
    )


def test_rain_gauge_totals_the_rain():
    from rain_gauge import RainGauge

    gauge = RainGauge("the meadow")
    gauge.record(4)
    gauge.record(11)
    got = (gauge.total, gauge.readings)
    assert got == (15, 2), (
        f"after record(4) and record(11), (total, readings) was {got}, expected (15, 2): "
        "add millimeters to self.total and 1 to self.readings"
    )


def test_trail_camera_keeps_the_animals():
    from trail_camera import TrailCamera

    camera = TrailCamera("the creek trail")
    camera.photograph("deer")
    camera.photograph("heron")
    got = (camera.animals, camera.last)
    assert got == (["deer", "heron"], "heron"), (
        f"after photograph('deer') and photograph('heron'), (animals, last) was {got}, "
        "expected (['deer', 'heron'], 'heron'): append the animal and store it as self.last"
    )


def test_creek_gauge_keeps_the_highest():
    from creek_gauge import CreekGauge

    creek = CreekGauge("French Creek")
    for level in (31, 52, 45):
        creek.record(level)
    got = (creek.levels, creek.highest)
    assert got == ([31, 52, 45], 52), (
        f"after recording 31, 52 and 45, (levels, highest) was {got}, expected ([31, 52, 45], 52): "
        "append the level, and store it as self.highest only when it is greater"
    )


def test_station_has_all_four():
    import main

    station = main.make_station()
    kinds = [type(thing).__name__ for thing in station]
    want = ["Feeder", "RainGauge", "TrailCamera", "CreekGauge"]
    assert kinds == want, (
        f"make_station returned objects of {kinds}, expected {want}: append feeder, gauge, camera "
        "and creek to station, in that order"
    )


def test_main_prints_every_report(capsys):
    import main

    main.main()
    output = capsys.readouterr().out
    want = [
        "Feeder at the pond: 6 birds",
        "Rain at the meadow: 15 mm over 2 readings",
        "Camera on the creek trail: 2 photos, the last a heron",
        "French Creek: 3 readings, highest 52",
    ]
    for line in want:
        assert line in output, f"the program did not print: {line}"


def test_pull_requests_were_merged():
    """One merged pull request per class file, plus one for main.py."""
    subjects = git("log", "--merges", "--format=%s").splitlines()
    merged = [subject for subject in subjects if "pull request" in subject.lower()]
    assert len(merged) >= 5, (
        f"Found {len(merged)} merged pull requests, expected at least 5: one for each of the four "
        "class files, then one for main.py. Merge with Merge pull request, not Squash and merge, "
        "and pull main before you run this check."
    )


def test_teammates_each_committed():
    """Commits to src after the starter come from at least two people."""
    roots = git("rev-list", "--max-parents=0", "HEAD").split()
    span = [f"{root}..HEAD" for root in roots] or ["HEAD"]
    authors = set(git("log", "--no-merges", "--format=%ae", *span, "--", "src").split())
    assert len(authors) >= 2, (
        f"Found commits to src from {len(authors)} email address(es). Each teammate commits "
        "their own file from their own computer."
    )


def test_no_todo_remains():
    for path in sorted(SRC.glob("*.py")):
        assert "TODO" not in path.read_text(encoding="utf-8"), (
            f"src/{path.name} still has a TODO marker: delete each one once its code is written, "
            "including the Author line"
        )
