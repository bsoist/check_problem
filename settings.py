import os.path
DEBUG = False # set to True to see the command for one student

# What is the path to this directory
BASE_DIR = os.path.join('/', 'Users', 'bill', 'cs50')

# In which subdirectory will you like to store other solutions
SOLUTIONS_DIR = os.path.join(BASE_DIR, 'source50')

# In which subdirectory would you like to store your students' code
STUDENT_DIR = os.path.join(BASE_DIR, 'compare_code', 'student_code')

# In which subdirectory will you store distribution code
DIST_DIR = os.path.join(BASE_DIR, 'compare_code', 'dist_code')

# map filenames that don't match the slug
# e.g. the filter problem actually checks a file called helpers.c
PROBLEM_NAMES = {
    'filter': 'helpers',
}

# No more editing needed (probably)
BASE_URL = 'git@github.com:me50/'

students = [line.strip() for line in open('students.txt')]
if DEBUG: students = students[:1]