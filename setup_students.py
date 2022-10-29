import os
import settings
import subprocess
PIPE = subprocess.PIPE

# Clone Repos
os.chdir(settings.STUDENT_DIR)
for student in settings.students:
    this_url = settings.BASE_URL + student + '.git'
    process = subprocess.Popen(
                ['git', 'clone', this_url], 
                stdout=PIPE,
                stderr=PIPE
    )
    stdoutput, stderroutput = process.communicate()



