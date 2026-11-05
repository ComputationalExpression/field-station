# Activity 9: Field Station

|Item |       |
|:----|:------|
|Released |Friday, November 6, in class |
|Due |Monday, November 9, 9:00am |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

The field station at the Bousson Environmental Research Reserve keeps track of what happens on
its land. Your team of three or four shares this one repository. The code is nearly all
written, so most of your time goes to the team workflow: each of you finishes one class, on your
own branch, and merges it through a pull request that a teammate approves. Then one of you
finishes `main.py`. If a step confuses you, please ask about it while you are still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this activity you should be able to:

* finish a method that changes an attribute of `self`
* work on a branch, open a pull request, review a teammate's, and merge it
* update `main` after a teammate's merge

## Your file

Each class is in its own file in `src`, with `__init__` and `report` written. What is left is
its recording method, marked `TODO`, plus your name on the `Author:` line:

|File |Class |Finish this method |
|:----|:-----|:------------------|
|`src/feeder.py` |`Feeder` |`visit(birds)`: add `birds` to `self.visits` |
|`src/rain_gauge.py` |`RainGauge` |`record(millimeters)`: add to `self.total`, and add 1 to `self.readings` |
|`src/trail_camera.py` |`TrailCamera` |`photograph(animal)`: append to `self.animals`, and store it as `self.last` |
|`src/creek_gauge.py` |`CreekGauge` |`record(level)`: append to `self.levels`, and keep the highest in `self.highest` |

Agree who takes which file. In a team of three, one of you takes two files, each on a branch of
its own with its own pull request. Methods that change an attribute are on
[Classes and Objects, slide 7](https://computationalexpression.com/slides/week-11-session-2/#7).

Each file runs by itself, and its last comment says what it should print:

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
2. **Finish your method** and put your name on the `Author:` line. Change only your file
3. **Commit and push your branch**: `git add` your file, `git commit`, then
   `git push -u origin your-name`, or **Publish Branch** in Source Control
4. **Open a pull request** on GitHub with **Compare & pull request**
   ([slide 6](https://computationalexpression.com/slides/week-11-session-3/#6))
5. **Review a teammate's pull request**, in a circle so that each of you reviews one: in
   alphabetical order by first name, each person reviews the next person's, and the last
   reviews the first. Open **Files changed**, comment on at least one line, then
   **Review changes**, **Approve**, and **Submit review**
6. **Merge your approved pull request** with **Merge pull request**, not Squash and merge
7. **Finish `main.py`.** Once all four classes are merged, one teammate updates `main`
   ([slide 7](https://computationalexpression.com/slides/week-11-session-3/#7)), makes a branch
   named `station`, appends the four objects to `station` in `make_station`, and puts every
   teammate's name on the `Author:` line. A teammate who did not write it reviews and approves
   that pull request, then it is merged
8. **Everyone updates `main`** with `git switch main` and `git pull`, then runs the program and
   the checks

### Example run

```text
$ uv run python src/main.py
==================================================
BOUSSON FIELD STATION
==================================================
Feeder at the pond: 6 birds
Rain at the meadow: 15 mm over 2 readings
Camera on the creek trail: 2 photos, the last a heron
French Creek: 3 readings, highest 52
```

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade. Each of you earns a checkmark by doing all three of these:

* push something to your branch
* open a pull request
* review at least one teammate's pull request

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

Your branch, your pull request, and your review are graded as they stand on GitHub at the
deadline. Please merge every pull request before then, then open your repository on GitHub and
confirm each class file and the finished `main.py` are on `main`.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
