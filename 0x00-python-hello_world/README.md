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

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
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

## Task 5. Print string (mandatory)

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
- The output of the program should be:
  - 3 times the value of `str`
  - followed by a new line
  - followed by the 9 first characters of `str`
  - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [5-print_string.py](5-print_string.py)

## Task 6. Play with strings (mandatory)

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

You can find the source code `here`
You are not allowed to use any loops or conditional statements.
You have to use the variables `str1` and `str2` in your new line of code
Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [6-concat.py](6-concat.py)

## Task 7. Copy - Cut - Paste (mandatory)

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters
```
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [7-edges.py](7-edges.py)

## Task: 8. Create a new sentence (mandatory)

Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.

- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
```
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [8-concat_edges.py](8-concat_edges.py)

# Task 9. Easter Egg (mandatory)

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
```
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
```
**Repo:**

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x00-python-hello_world`
- File: [9-easter_egg.py](9-easter_egg.py)