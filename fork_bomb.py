import os
import time

while (True):
	time.sleep(10)
	pid = os.fork()

	if (pid == 0):
		print("New child born!")

# Fork bomb - do not run it with unsaved data!
