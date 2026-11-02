# Activity 9: Field Station

|Item |       |
|:----|:------|
|Released |Friday, November 6, in class |
|Due |Monday, November 9, 9:00am |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

The field station at the Bousson Environmental Research Reserve keeps track of what happens on
its land. Your team of three or four shares this one repository. Each of you writes a class for one thing the
station tracks, in your own file, on your own branch, and merges it through a pull request that
a teammate approves. Then one of you brings every class together in `main.py`. If a step
confuses you, please ask about it while you are still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this activity you should be able to:

* write a class with `__init__`, attributes, and methods, in a file of its own
* import a class from another file
* work on a branch, open a pull request, review a teammate's, and merge it

## Your class

Each teammate picks a different thing the station tracks, such as birds at a feeder, rain,
hikers on a trail, photos from a trail camera, or the level of the creek. Agree as a team who
takes which. Your class goes in its own file in `src`, named for the thing, such as
`src/feeder.py`, and has:

* `__init__`, which stores each starting value as an attribute of `self`
  ([Classes and Objects](https://computationalexpression.com/slides/week-11-session-2/#3), slide 3)
* a method that records something by changing an attribute
  ([slide 8](https://computationalexpression.com/slides/week-11-session-2/#8))
* `report(self)`, which returns one line of text about the object, with `return`, not `print`

To try your class before the pull request, add an `if __name__ == "__main__":` block at the
bottom of your file that makes an object, records something, and prints its report. Run it:

```text
uv run python src/feeder.py
```

## Steps

The slides for each step are
[Working as a Team on One Repository](https://computationalexpression.com/slides/week-11-session-3/).

1. **Make your branch**, named for you
   ([slide 5](https://computationalexpression.com/slides/week-11-session-3/#5)):
   `git switch -c your-name`, or click the branch name at the bottom left of VS Code and
   choose **Create new branch**
2. **Write your class** in your own file. Do not change `main.py` yet
3. **Commit and push your branch**: `git add` your file, `git commit`, then
   `git push -u origin your-name`, or **Publish Branch** in Source Control
4. **Open a pull request** on GitHub with **Compare & pull request**
   ([slide 6](https://computationalexpression.com/slides/week-11-session-3/#6))
5. **Review a teammate's pull request**, in a circle so that each of you reviews one: in
   alphabetical order by first name, each person reviews the next person's, and the last
   reviews the first. Open **Files changed**, comment on at least one line, then
   **Review changes**, **Approve**, and **Submit review**
6. **Merge your approved pull request** with **Merge pull request**, not Squash and merge
7. **Bring the station together.** Once every class is merged, one teammate updates `main`
   ([slide 7](https://computationalexpression.com/slides/week-11-session-3/#7)), makes a branch
   named `station`, and in `main.py` imports each class, makes an object of each in
   `make_station`, records something in it, and appends it to `station`. Put every teammate's
   name on the `Author:` line and delete each `TODO`. A teammate who did not write it reviews
   and approves that pull request, then it is merged
8. **Everyone updates `main`** with `git switch main` and `git pull`, then runs the program and
   the checks

### Example run

```text
$ uv run python src/main.py
==================================================
BOUSSON FIELD STATION
==================================================
Rain at the meadow: 15 mm over 2 readings
Camera on the creek trail: 2 photos, the last a heron
```

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade. Each teammate's grade comes from their own class, their own pull request, and
the review they gave. What is graded is the attempt, not whether every value comes out right.

|Level |What it looks like |
|:-----|:------------------|
|**Complete** |At least half of the activity is done |
|**Partial** |Less than half is done, but something beyond the starter was committed |
|**Incomplete** |Nothing was changed |

Run the automated checks yourself, as many times as you like, from the top folder of this
repository rather than from inside `src`, after `git pull` on `main`:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says what to look at when it fails. Under a failed check, gatorgrade
also prints a `uv run pytest ...` command. Run it: the last lines say what was found and what
was expected.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

## Submitting

The `main` branch on GitHub at the deadline is what gets graded, so merge every pull request
before then. Open your repository on GitHub and confirm each class file and the finished
`main.py` are on `main`.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
