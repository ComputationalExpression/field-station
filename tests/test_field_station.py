"""Checks for Activity 9: Field Station.

The class checks read every file in src except main.py, so they work for a team of any size.
The git checks read the repository's history: the merges GitHub makes for pull requests, and
who committed the class files.
"""

import ast
import subprocess
from pathlib import Path

import main

SRC = Path(__file__).resolve().parent.parent / "src"


def class_files():
    """Return every Python file in src except main.py."""
    return sorted(path for path in SRC.glob("*.py") if path.name != "main.py")


def classes_in(path):
    """Return the class definitions at the top level of a file."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def every_class():
    """Return (file name, class) for every class in the class files."""
    found = []
    for path in class_files():
        for cls in classes_in(path):
            found.append((path.name, cls))
    assert len(found) > 0, (
        "No class was found in src. Each teammate writes a class in a separate file in src, "
        "such as src/feeder.py."
    )
    return found


def methods_of(cls):
    """Return the methods of a class by name."""
    return {node.name: node for node in cls.body if isinstance(node, ast.FunctionDef)}


def is_self_attribute(node):
    """Return True for self.something."""
    return (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "self"
    )


def changes_self(method):
    """Return True when a method assigns to, adds to, or appends to an attribute of self."""
    for node in ast.walk(method):
        if isinstance(node, ast.Assign) and any(is_self_attribute(t) for t in node.targets):
            return True
        if isinstance(node, ast.AugAssign) and is_self_attribute(node.target):
            return True
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and is_self_attribute(node.func.value)
        ):
            return True
    return False


def git(*args):
    """Run a git command in the repository and return its output."""
    result = subprocess.run(
        ["git", *args], cwd=SRC.parent, capture_output=True, text=True, check=False
    )
    return result.stdout


def test_each_teammate_has_a_class_file():
    """At least two class files, each with a class in it."""
    files = class_files()
    names = ", ".join(path.name for path in files) or "none"
    assert len(files) >= 2, (
        f"Found these files in src besides main.py: {names}. "
        "Each teammate adds a file of their own, so a team has at least two."
    )
    for path in files:
        assert classes_in(path), f"src/{path.name} has no class in it."


def test_each_init_sets_attributes():
    """Every class has __init__, and it sets an attribute of self."""
    for name, cls in every_class():
        methods = methods_of(cls)
        assert "__init__" in methods, f"Class {cls.name} in src/{name} has no __init__ method."
        assert changes_self(methods["__init__"]), (
            f"The __init__ of {cls.name} in src/{name} sets no attribute. "
            "Store each starting value as self.something."
        )


def test_each_class_has_a_method_that_records():
    """Every class has a method besides __init__ and report that changes an attribute."""
    for name, cls in every_class():
        others = [
            method
            for method_name, method in methods_of(cls).items()
            if method_name not in ("__init__", "report")
        ]
        assert any(changes_self(method) for method in others), (
            f"{cls.name} in src/{name} needs a method besides __init__ and report that changes "
            "one of its attributes, such as self.visits += birds."
        )


def test_each_report_returns_a_string():
    """make_station returns objects whose report method returns text."""
    station = main.make_station()
    assert len(station) > 0, "make_station returned an empty list. Append an object of each class."
    for thing in station:
        text = thing.report()
        assert isinstance(text, str) and text.strip(), (
            f"report() of {type(thing).__name__} returned {text!r}. "
            "Use return with a string, not print."
        )


def test_station_has_every_class_file():
    """make_station has an object from every class file."""
    files = class_files()
    assert files, "There are no class files in src yet, so make_station has nothing to bring together."
    used = {type(thing).__module__ for thing in main.make_station()}
    for path in files:
        assert path.stem in used, (
            f"make_station has no object from src/{path.name}. "
            f"Import its class in main.py and append an object of it to station."
        )


def test_main_prints_every_report(capsys):
    """main prints the report of every object."""
    main.main()
    output = capsys.readouterr().out
    reports = [thing.report() for thing in main.make_station()]
    assert reports, "make_station returned an empty list, so main printed no reports."
    for report in reports:
        assert report in output, f"main did not print this report: {report!r}"


def test_pull_requests_were_merged():
    """One merged pull request per class file, plus one for main.py."""
    subjects = git("log", "--merges", "--format=%s").splitlines()
    merged = [subject for subject in subjects if "pull request" in subject.lower()]
    needed = max(len(class_files()), 2) + 1
    assert len(merged) >= needed, (
        f"Found {len(merged)} merged pull requests, and this team needs {needed}: one for each "
        "class file, then one for main.py. Merge with Merge pull request, not Squash and merge, "
        "and pull main before you run this check."
    )


def test_teammates_each_committed_a_class():
    """Commits to the class files come from at least two people."""
    log = git("log", "--no-merges", "--format=%ae", "--", "src", ":(exclude)src/main.py")
    authors = set(log.split())
    assert len(authors) >= 2, (
        f"Found commits to the class files from {len(authors)} email address(es). Each teammate "
        "commits their own class file from their own computer."
    )
