# Python for Data Analysts - Homework

Practice tasks and homework for the course Python for Data Analysts. Every task
checks your code and prints `OK`, `FAIL` or `TODO` for each check, and a final
line such as `5 of 7 checks passed`.

The lectures: https://ivapopova-courses.github.io/Python-Data-Analysts-UniCredit-Slides/

You need [Python](https://www.python.org/downloads/) 3.12 or newer, VS Code and Git.
Step by step:
https://ivapopova-courses.github.io/Python-Data-Analysts-UniCredit-Slides/how-to#practice-and-homework

## Set it up once

You clone this repository and keep it as `upstream` - new tasks come from there.
Your own repository is `origin` - your solutions go there.

1. On GitHub, create a new **empty** repository of your own (private is fine) -
   without a README, licence or `.gitignore`.
2. In a terminal:

   ```bash
   git clone https://github.com/ivapopova-courses/Python-Data-Analysts-UniCredit-Homework.git
   cd Python-Data-Analysts-UniCredit-Homework
   git remote rename origin upstream
   git remote add origin https://github.com/<your-user>/<your-repo>.git
   git push -u origin main
   ```

3. Create the virtual environment and install the libraries (Windows; on macOS /
   Linux use `python3 -m venv .venv` and `source .venv/bin/activate`):

   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Open the folder in VS Code and choose the interpreter in `.venv`
   (`Ctrl+Shift+P` > **Python: Select Interpreter**).

Check the remotes with `git remote -v`: `upstream` is this repository, `origin`
is yours.

## Run a task

Run commands from the root folder of the repository (the folder with this README),
with the virtual environment active:

```bash
python 01-intro-syntax-types/practice/task1-first-values.py
python 01-intro-syntax-types/homework.py
```

Edit only the parts of the files that the comments ask you to change: the lines
between `# ---- your code ... ----` and `# ---- end of your code ----`.

How to read the output:

- a line `-- Part N: ... ---` starts the checks of each part of the task;
- `OK` (green): your code gives the expected value;
- `FAIL` (red): it does not - the lines `got:` and `expected:` under it show
  what your code gave and what the check expects;
- `TODO` (yellow): you have not written any code in this part yet;
- at the end: one line per part, then `N of M checks passed`.

In a predict task (`*predict*.py`) you replace each `"?"` with the value you
expect. It prints `OK`, `WRONG` or `TODO` (not answered yet) - never the real
result, so run it as often as you like.

## Save your work

```bash
git add .
git commit -m "Session 1 practice"
git push
```

## Get the new tasks

New lecture folders are added before each session. Commit your work first, then:

```bash
git pull --no-rebase --no-edit upstream main
git push
```

Existing files are not changed after they are published, so the pull does not
conflict with your work.

## Layout

```text
check.py                       prints OK / FAIL / TODO and the final summary
.starters.json                 the starter code of each task (check.py uses it for TODO)
requirements.txt               the libraries of the course (pip install -r requirements.txt)
data/                          the made-up sample data (loans, clients, rating scale)
NN-topic/practice/taskN-*.py   practice tasks of lecture NN
NN-topic/homework.py           homework of lecture NN
```

What is in the data files: https://ivapopova-courses.github.io/Python-Data-Analysts-UniCredit-Slides/sample-data

---

Built with Claude Opus 5.5 via Claude Code. Published by [SciScend](https://sciscend.com/).
