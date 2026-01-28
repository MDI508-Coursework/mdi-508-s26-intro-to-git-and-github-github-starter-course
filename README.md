# MDI-508-S26 Homework 0: Introduction to Git, GitHub, and GitHub Classroom

**Due: February 5, 2026. 11:59 pm**

This assignment is designed to introduce you to the basic workflow for using Git, GitHub, and Github Classroom, which we
will use throughout the course for submitting homework assignments.  By the end of this homework, you will have:

- Created or verified a GitHub account
- Joined the course GitHub Classroom
- Cloned a repository to your local machine
- Edited a file locally
- Committed and pushed your changes to GitHub
- Viewed automated feedback from GitHub Classroom

## 1. What are Git, GitHub, and GitHub Classroom?

Git is a version control system used primarily for code. It tracks changes to files over time and allows you to:

- Keep a complete history of your work
- Revert to earlier versions if needed
- Collaborate with others in a structured way

GitHub is an online platform that hosts Git repositories.  A **repository** (often shortened to *repo*) is a collection
of files together with their full change history tracked by Git. In this course, each homework assignment lives in its
own repository, which exists both locally on your computer (when you clone it) and remotely on GitHub, where it is
stored, shared, and automatically graded.

GitHub also provides provides tools for writing code, collaboration, review, and automation.

In this course:

- Each homework assignment will be a GitHub repository;
- Submitting homework means "pushing commits" to GitHub -- think of this like saving your code to online into Github.
- Many of the problems in an assignment will be automatically graded using GitHub Classroom.

For a more detailed introduction to submitting assignments using GitHub Classroom, you should consult the following
tutorials:

- GitHub Docs: Git and GitHub basics  
  <https://docs.github.com/en/get-started/start-your-journey/about-github-and-git>

- GitHub Hello World tutorial (browser-based, no installation required)  
  <https://docs.github.com/en/get-started/start-your-journey/hello-world>

> Note: The GitHub Hello World tutorial above introduces a general GitHub workflow that includes many steps such as
> creating new repositories, creating branches, opening pull requests, and merging changes. For the purposes of this
> course, however, you do **not** need to know how to do these steps. GitHub Classroom automatically creates the
> repository for you, and submission is done by committing and pushing directly to the main branch.

## 2. Join GitHub and accept the assignment

To get started, you need a GitHub account. If you already have a GitHub account you wish to use for this course, you may
skip this step. Otherwise, go to <https://www.github.com> to create a new account.

Remain logged into GitHub in your browser for the rest of this assignment. Once logged in, you can click on the
following GitHub Classroom Homework 0 assignment link:

   <https://classroom.github.com/a/NlBgokNe>

(*Note that, for future assignments, the GitHub Classroom assignment link will be posted on the course website.*)

When prompted, authorize GitHub Classroom to access your GitHub account, then select your UB ID from the course roster
if asked. Then accept the assignment.  After accepting, GitHub Classroom will create your own private repository for
this homework, and you will be provided a link to this repository. Click on that link, and you will be taken to the
repository's page on GitHub. This repository is your own homework assignment solution that you will edit and submit by
"pushing" the edits to it.

Specifically, you will edit a repository by editing files in that repository, or by creating new files. These edits
can be done online directly in your browser using GitHub’s built-in editor or GitHub Codespaces, or you can do them
offline on your own computer, and then push them back online into GitHub. Once edits are made, you must push them back
onto GitHub. Pushing edits back onto GitHub saves a snapshot of your code on the cloud. When developing code (for this
class or in general) you should push often to save your progress online. You will not be penalized by multiple pushes/
submissions. Your grade will only be based on the last submission you push prior to the deadline.

## 3. Setting up your programming environment

To complete this homework, you will need a way to create and edit Python files in the repository, and submit changes to
back GitHub. Up to this point, you may have only written Python code inside Jupyter notebooks. For this course, you will
also work with plain Python files (`.py`). This requires a code editor or integrated development environment (IDE).

There are three supported options for this course. Any one of them is acceptable.

### Option A: Edit files directly on GitHub (simple browser editor)

This option uses GitHub’s built-in file editor, accessed by clicking the pencil icon on a file on GitHub. It behaves
like a very simple text editor and is best suited for small or straightforward changes.

1. Open your Homework 0 repository on GitHub in your browser.
2. Click a file to edit, if it exists(for example, `hw0.py`), then click the pencil icon to edit.  If it doesn't exist,
click the "Add file" button at the top to create the new file. Be sure to name it.
3. Once you start to edit a file, or create a new one, you will be taken to the browser-based text editor.
4. Make your changes to the file.
5. Commit the changes using the green "Commit changes..." button.

Committing the changes will trigger a push to Github and the GitHub autograder. Consult the following page for details

  <https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files>

### Option B: GitHub Codespaces (in-browser IDE)

GitHub Codespaces provides a full-featured development environment that runs entirely in your browser. It looks and
behaves very similarly to Visual Studio Code (see below), but requires no installation on your computer.

With Codespaces, you get:

- A full code editor with syntax highlighting and file navigation
- An integrated terminal
- The ability to run and debug code and tests in the browser, prior to submitting your file to the autograder.

To create a Codespace for your repository:

1. Open your Homework 0 repository on GitHub
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**

This will take you to the browsdwer-based development environment. From you, you can create and edit files, run
commands, and then commit and push your code. Note that **you must commit and push your code you develop inside
Codespace** to save any of your results, so be sure to do this often if you plan to work in Codespaces.  Any commits you
make inside Codespaces are committed and pushed to your GitHub Classroom repository and will trigger autograding.

More information about the Codespaces environment can be found here:

- Quickstart guide: <https://docs.github.com/en/codespaces/quickstart>
- More detailed information about developing in Codespace: <https://docs.github.com/en/codespaces/developing-in-a-codespace>
- Specific information about how to commit and push your changes:
<https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace>

### Option C: Use Visual Studio Code (VS Code) on your computer (local)

Visual Studio Code (VS Code) is a free, widely used code editor that runs locally on your computer. You can download
it here: <https://code.visualstudio.com>.

VS Code looks and feels very much like Github Codespaces. This option gives you more control and is closer to
professional development workflows, but it requires additional setup to make sure you have things correctly installed
and cloned into your local computer.  Specifically, with this option, you must install and configure the following on
your local computer:

- Visual Studio Code (the code editor itself)
- Git (the version control software that will manage the local copy of your repository, as well as manage pushing to and
pulling / cloning from GitHub.
- Git authentication with GitHub (using SSH keys) to enable communication between your computer and GitHub.

Please refer to the following tutorials to perform these three tasks

- Installing VS Code  
  <https://code.visualstudio.com/docs/setup/setup-overview>

- Using Git with VS Code  
  <https://code.visualstudio.com/docs/sourcecontrol/overview>

- Generating and adding SSH keys for GitHub  
  <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>

Coding in VS Code is similar to coding on the GitHub Codespaces environment. Here is a tutorial to get you started:

- Python in VS Code (editing and running `.py` files)  
  <https://code.visualstudio.com/docs/python/python-tutorial>

Once configured, you will use Git to move changes between your computer and GitHub. There are two equivalent ways to do
this in VS Code (after you have set up your SSH keys on GitHub).

#### Option C1: Using the command line

- Clone your repository using `git clone`. This will download the repository onto your computer. In order to do this,
you will need your repo's URL, which you can find if you click the green "Code" button on the repo's webpage, then
copying the URL listed under the SSH tab. It should look something like:

`git@github.com:MDI508-Coursework/mdi-508-s26-intro-to-git-and-github-github-starter-course-YOUR_USER_NAME.git`

Once you have this, you can run the `git clone` command within your favorite terminal application (including the
terminal application that is inside VS code).

  ```bash
  git clone git@github.com:MDI508-Coursework/mdi-508-s26-intro-to-git-and-github-github-starter-course.git
  ```

This will copy the repository into your current working directory. Open this repository folder in VS Code.

- Make your edits to this repository.

- Stage changes with `git add` -- staging is like a step before committing your edits. For example, if you added
or edited a file `hw0.py`, you would save it then stage it using the command

  ```bash
  git add hw0.py
  ```

- Create commits with `git commit` -- committing is like finalizing the project "snapshot" that will be saved on your
computer and GitHub.  When you commit, you need to include a short message to state what this snapshot contains

  ```bash
  git commit -m "Added solution to HW problem 3
  ```

- Upload your work to GitHub with `git push` -- pushing the updated repository moves the edits from your computer to
GitHub.

  ```bash
  git push
  ```

Consult the following tutorial to learn more about the specific `git commands described above`:

- <https://docs.github.com/en/get-started/git-basics>

#### Option C2: Using VS Code’s built-in version control

VS Code includes built-in support for Git in the version-control tab on the left-side of the editor. Using this,
you can perform the above tasks entirely within VS Code.  Both approaches produce the same result: commits pushed to
your GitHub Classroom repository.

Refer to this tutorial for details: <https://code.visualstudio.com/docs/sourcecontrol/quickstart>

## 4. Editing your files

Regardless of your chosen environment, you will need to possibly clone your repository and then create, edit, commit and
push files into your repository and on GitHub. The different environments have different ways of doing this and you
should consult the apppropriate documentation we have linked to above to discuss how to do so. Here, we point out
a few important extra details for writing up your homework solutions.

### Reading inputs from the command line

For this and other homework assignments, you will often have to write Python programs that are able to receive different
inputs, and these inputs are passed in from the **command line**. Therefore, your solutions must be able to read these
inputs from the command line and do the required processing as detailed in the homework. Specifically, when you submit
your code to the autograder by pushing it onto Github, the autograder will test your solutions by running commands such
as

``` bash
python hw0.py 7 30
```

Here, the inputs `7` and `30` are command line arugments, and could be replaced with other inputs during grading. Your
program must be able to read these values and process them accordingly.  Below is a example code that would be placed
inside its own Python file , the name of which must adhere to whatever is specified in the homework. The code contains
the basic structure you need to read arguments from the command line, and then pass the values you read into whatever
processing you are required to implement for your homework. You should follow this pattern for your solutions:

>> Example Problem: Write a Python script named `calc_square.py` that takes in one integer value from the command line
>> and prints the square of that number. It should be invoked as
>>
>> ```
>> python calc_square.py 3
>> 9
>> ```

Then you would create a new python file name `calc_square.py` and place the following code inside of it:

```python
# Inside calc_square.py
import sys

def square(x):
  return x * x

# This line reads one argument from the command line, and converts that into an integer
n = int(sys.argv[1])

# Call a function that performs the computation
result = square(n)

# Print the result
print(result)
```

The line `import sys` gives access to command-line arguments. In particular, the variable `sys.argv` is a list of
strings, with `sys.argv[0]` is the name of the script (`calc_square.py`) and `sys.argv[1]` is the first argument passed.
on the command line. If we needed to read more arguments from command line, they would be located in `sys.argv[2]`,
`sys.argv[3]`, etc.

### Other files that may be graded

Besides the results of the various Python scripts you write, you may also be asked to add files to the repository. Often
these are plots produced by your code. If your code generates such plots, instead of printing some text, you will need
to save these plots, and then commit and push the saved files into your repository and onto GitHub.

Similarly, we may have some problems that will require you to submit a written solution, typically involving some hand
word math problems. You can type up such solutions with whatever software you choose, or submit a carefully scanned
copy of your hand-writte notes. These solutions must be legible in order to be graded. Like the plots, such files
need to be committed and pushed into your repository.

## 5. Receiving feedback from the autograder

Every time you commit and push changes to your repository on GitHub, the GitHub Classroom autograder will run
automatically. You do not need to submit anything separately. Pushing your code *is* the submission.

To view feedback on your submission:

1. Go to your Homework 0 repository on GitHub in your browser.
2. Click the **Actions** tab near the top of the page.
3. You will see a list of workflow runs. Click on the most recent one.
4. The workflow will show whether the autograder passed or failed:
   - A green checkmark indicates success.
   - A red ❌ indicates that one or more tests failed.
5. Click on the job name to view detailed output from the autograder.

If a test fails, read the error message carefully. You can fix your code and push again as many times as you like before
the deadline. Only the **last commit pushed before the deadline** will be graded.

The visible autograder tests are provided to help you debug and verify your work. Your final grade may also depend on additional tests and inputs that are not disclosed.

## 6. Programming problems for Homework 0 (5 points total)

In this homework, you will complete a small set of basic Python programming tasks. Each task is worth **1 point**, for a
total of **5 points**. These are intentionally simple and are meant to verify that you can edit code, commit it, push it
to GitHub, and view automated feedback.  You are allowed to use **Numpy** for this assignment. Do not use other
third-party Python libraries. Standard Python libraries such as `sys` are allowed.

### Task 1 (1 point): Hello, world

Implement a Python script named `hello_world.py` that accepts no command line arguments, and simply prints the
string `Hello, world!`.

Example usage:

```bash
python hello_world.py
# output:
Hello, world!
```

### Task 2 (1 point): Greeting with a name

Implement a Python script named  `greeting.py` that reads a name (one string, no spaces) from the command line, and
prints the string `Hello, $NAME!`, where `$NAME` is replaced with the name that is passed in from the command line.

Example usage:

```bash
python greeting.py Alice
# output:
Hello, Alice!
```

### Task 3 (1 point): Even or odd

Implement a Python script named `even_or_odd.py` that reads one integer from the command line and prints either
`even` or `odd`.

Example usage:

```bash
python even_or_odd.py 4
# output:
even
```

```bash
python even_or_odd.py 7
# output:
odd
```

### Task 4 (1 point): Sum a list

Implement a Python script named `sum_csv.py` that reads a filename from the command line, reads a CSV file containing a
single line of comma-separated numbers, and prints the sum of the numbers. Report your sum as an integer, perhaps using the `int()` function to do so.

You to debug your code, you should create a CSV file named `prob4-data-debug.csv` in your repository to test your code.
This file should contain a single line of comma-separated values, for example:

```
1,2,3,4
```

Example usage:

```bash
python sum_csv.py prob4-data-debug.csv
# output:
10
```

You do no not need to include the csv file in your repository.

Helpful Numpy functions:

- `numpy.loadtxt` (read comma-separated values): <https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html>
- `numpy.genfromtxt` (robust CSV reading): <https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html>
- `numpy.sum` (sum values): <https://numpy.org/doc/stable/reference/generated/numpy.sum.html>

### Task 5 (1 point): CSV shape (rows and columns)

Implement a Python script named `csv_shape.py` that reads a filename from the command line, reads the CSV file, and
prints two integers: the number of rows and the number of columns, separated by a single space.

Example output format:

```
3 5
```

You should create a CSV file named `prob5-data-debug.csv` in your repository to test your code. This file can contain
any rectangular table of values. For example, the following file has 3 rows and 4 columns:

`prob5_data.csv`

```
1,2,3,4
5,6,7,8
9,10,11,12
```

Example usage:

```bash
python csv_shape.py prob5-data-debug.csv
# output:
3 4
```


- `ndarray.shape` (rows, columns): <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html>

Each task is graded independently. You may commit and push as many times as you like before the deadline. Only the final state of your repository will be graded.

## 7. Stage, commit and push your changes

Regardless of which editing environment you use, **your work is submitted by committing and pushing changes to GitHub**.
You do not upload files separately and you do not email submissions.

Below are instructions for staging, committing, and pushing your work for each of the three supported workflows.

### Option A: GitHub browser editor (pencil icon)

When you edit files directly on GitHub using the browser editor:

1. Open a file in your repository and click the pencil icon.
2. Make your edits in the browser.
3. Scroll to the bottom of the page.
4. Enter a short commit message describing your change.
5. Click **Commit changes**.

This automatically:

- stages the changes,
- creates a commit,
- and pushes it to GitHub.

No additional steps are required. Pushing the commit triggers the autograder.

Tutorial:

- Editing and committing files on GitHub  
  <https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files>

### Option B: GitHub Codespaces

When working inside a GitHub Codespace, you must explicitly commit and push your changes.

#### Using the terminal in Codespaces

1. Save your edited files.
2. Open the terminal inside the Codespace.
3. Check the status of your files:

   ```bash
   git status
   ```

4. Stage your changes:

   ```bash
   git add <filename>
   ```

   or stage everything:

   ```bash
   git add .
   ```

5. Commit your changes:

   ```bash
   git commit -m "Describe your changes"
   ```

6. Push to GitHub:

   ```bash
   git push
   ```

#### Using the Source Control panel in Codespaces

1. Click the **Source Control** icon on the left sidebar.
2. Review the changed files.
3. Stage the changes.
4. Enter a commit message.
5. Click **Commit**, then **Push**.

Tutorials:

- Using source control in Codespaces  
  <https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace>

### Option C: VS Code on your computer (local)

When working locally, commits and pushes move changes from your computer to GitHub.

#### Using the command line

1. Save your files.
2. Open a terminal in the repository directory.
3. Check status:

   ```bash
   git status
   ```

4. Stage files:

   ```bash
   git add <filename>
   ```

5. Commit:

   ```bash
   git commit -m "Describe your changes"
   ```

6. Push:

   ```bash
   git push
   ```

#### Using VS Code’s built-in Git interface

1. Open the repository folder in VS Code.
2. Click the **Source Control** icon.
3. Review changed files.
4. Stage the changes.
5. Enter a commit message.
6. Click **Commit**, then **Push** or **Sync Changes**.

Tutorials:

- Using Git with VS Code  
  <https://code.visualstudio.com/docs/sourcecontrol/overview>
- Git basics  
  <https://docs.github.com/en/get-started/git-basics>

You may commit and push as many times as you like before the deadline. The autograder runs on every push, and **only the
final state of your repository before the deadline will be graded**.
