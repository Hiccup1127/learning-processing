import os
import sys
import time

pid = os.fork()

if (pid==0):

	for i in range(1,6):
		print(f"[Child] step {i}")
		time.sleep(1)

	time.sleep(10)
	sys.exit(0)

else:

	for i in range(1,8):
		print(f"[Parent] step {i}")
		time.sleep(1)

	print(os.waitpid(pid, os.WNOHANG)) # just checks child without freezing
#	print(os.wait()) # freezes parent until child is dead

	time.sleep(5)
