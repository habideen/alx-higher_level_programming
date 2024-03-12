# 0x00. Python - Hello, World

- Python
- By: Guillaume
- Weight: 1
- Project will start Mar 11, 2024 6:00 AM, must end by Mar 12, 2024 6:00 AM
- Checker was released at Mar 11, 2024 12:00 PM
- An auto review will be launched at the deadline

## Concepts

For this project, we expect you to look at this concept:

- [The Python Tutorial](https://intranet.alxswe.com/rltoken/Fl7kjKxXgkbmX5P0-4k4tQ)
- [Python Programming: An Introduction to Computer Science 3rd edition](https://intranet.alxswe.com/rltoken/NHlaFZoFcYtZHVMj1ncXmw)
- [Derek Banas’ Learn to program](https://intranet.alxswe.com/rltoken/RNQj-DQDjG_lOzQn_ku2eg)
- [The Python Guru](https://intranet.alxswe.com/rltoken/5U-qFDOGHyBSCLg2A37ILA)
- [New string formatting](https://intranet.alxswe.com/rltoken/SUwBgkKMH7wiedG57WcT9A)
- [Garbage collector](https://intranet.alxswe.com/rltoken/CimKF3MlfErabvZWtFxHjg)
- [Python Interpreter](https://intranet.alxswe.com/rltoken/a5z3uSkiby1Xw679cFiw1Q)
- [Python bytecode](https://intranet.alxswe.com/rltoken/oJ2v8bVCLZmAowJ7WXLzJg)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

### General

- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- `A README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.\*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l` file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### C Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be - different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## Pycodestyle

`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

## Tasks 0. Run Python file (mandatory)

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

```guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

- GitHub repository: alx-higher_level_programming
- Directory: 0x00-python-hello_world
- File: [0-run](0-run)

## Task 1. Run inline (mandatory)

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Best School: 98
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [1-run_inline](1-run_inline)


## Task 2. Hello, print (mandatory)

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

GitHub repository: `alx-higher_level_programming`
Directory: `0x00-python-hello_world`
File: [2-print.py](2-print.py)

## Task 3. Print integer (mandatory)

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
  - the number, followed by `Battery street`,
  - followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$
```

**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [3-print_number.py](3-print_number.py)

## Task 4. Print float (mandatory)

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

- You can find the source code here
- The output of the program should be:
  - Float:, followed by the float with only 2 digits
  - followed by a new line
= You are not allowed to cast number to string
= You have to use f-strings
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [4-print_float.py](4-print_float.py)