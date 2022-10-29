# Check Problem

This is very rough tool I've used to check student work against a collection of previous submissions and solutions online. 

Over a couple of years, it became a little too hacky for me and I started the process of re-factoring it. 

I have not used it since, but I believe it still works if used carefully.

## Overview

### Distribution Code

A directory which contains any distribution code for each problem you want to check.

### Solutions Archive

A directory which contains a subdirectory for each problem (named for the problem). Each of those directories should have subdirectories each of which contains a solution to the problem (named for the problem).

It should make sense once you have tried to use this.

I use a git repo which I forked from another maintained by [dkiang](https://github.com/dkiang) and I store this in a directory that is a sibling of this directory. These solutions **SHOULD NOT** be published online! I keep them in a directory which is a sibling of this directloy and I highly recommend doing that. If you don't, you'll need to adjust your settings in `settings.py`

### Student Code

An empty directory which will contain your students' code. You will use the `setup_students.py` script here to clone your students' repos to this directory.

## Setup

1. Ensure `settings.py` is configured for your directory and path names
1. Ensure each of your students has submitted at least one problem using `submit50`.
1. Add the GitHub usernames for each of your students to `students.txt` one per line.
1. Run `setup_students.py` using Python 3

## Checking Problems

1. Esure you've added any distribution code to the correct directory.
1. Run `check_problem.py` passing the `submit50` slug as the only argument
1. The script produces a lot of output, some(much?) of which is impossible to read.
1. You should find a directory named `f{problem_name}_results` 
1. Navigate to that folder and launch `index.html` to view results

