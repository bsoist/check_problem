import os
import sys
import settings
import subprocess
PIPE = subprocess.PIPE

try:
	problem_slug = sys.argv[1]
except:
	print("Please provide problem slug")
	exit()
try:
	slug_parts = problem_slug.split('/')
	which_problem = slug_parts.pop()
	if which_problem in ['less', 'more']:
		problem_name = slug_parts.pop()
		problem_folder= os.path.join(problem_name, which_problem)
	else:
		problem_folder = problem_name = which_problem
	problem_name = settings.PROBLEM_NAMES.get(problem_name, problem_name)
except:
	print("Unexpected error")
	exit()

# Pull code
os.chdir(settings.STUDENT_DIR)
for student in settings.students:
	os.chdir(student)
	process = subprocess.Popen(['git', 'pull'], stdout=PIPE, stderr=PIPE)
	stdoutput, stderroutput = process.communicate()
	print(stdoutput)
	print(stderroutput)
	process = subprocess.Popen(
				['git', 'checkout', problem_slug],
				stdout=PIPE,
				stderr=PIPE
	)
	stdoutput, stderroutput = process.communicate()
	print(stdoutput)
	print(stderroutput)
	os.chdir('..')

# compare50 this/years/submissions/* \
# -a last/years/submissions/* \ 
# -d distro/code/* 

os.chdir('..')
submissions = os.path.join(settings.STUDENT_DIR, '*', f'{problem_name}.c')
other_submissions = os.path.join(
						settings.SOLUTIONS_DIR,
						problem_folder,
						'*',
						f'{problem_name}.c'
)
command = ['python3.9', '-m', 'compare50', submissions, '-a', other_submissions]
dist_code_file = os.path.join(settings.DIST_DIR, f'{problem_name}.c')
if os.path.exists(dist_code_file):
	command.append('-d')
	command.append(dist_code_file)
if settings.DEBUG:
	print(' '.join(command))
	exit()
print(' '.join(command))
process = subprocess.Popen(command, stdout=PIPE, stderr=PIPE)
stdoutput, stderroutput = process.communicate()
print(stdoutput)
print(stderroutput)
os.rename('results', f'{problem_name}_results')



