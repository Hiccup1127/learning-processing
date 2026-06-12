import os
import sys
import time

pid = os.fork()

if (pid==0):
	print(f"[Child {os.getpid()}]")

	time.sleep(2)
	sys.exit(0)

print(f"[Parent {os.getpid()}] waiting for child {pid}")

os.wait()


print("end.")



# As I founded in internet: Process - a running instance of a program
# being executed by an operating system.
# Multiprocessing - running the entire copy of a process at the same time.

# Here, os.fork, creates another copy of a program. It starts from the line
# pid=os.fork() [including this line], and goes down to the end. And since this moment,
# there is parent process, and child process. pid (variable) of parent contains the
# pid of it's child, while parent's os.getpid() shows pid of parent process.
# Child's pid (variable) is equal to 0, while os.getpid() will show it's actual pid.
# If child won't return 0 status at the end of If block, then it will do all from
# the line where it's been created, to the end. os.wait() - is the function that
# handles the child's exit and returning its status. so the parent process
# will step over if statement, but run all the code until os.wait() line,
# then it'll wait for it's child process.
