import os
import time

pid = os.fork()

if (pid == 0):
	while (True): print(1)
else:
	print("Hello, I'm parent!")
	time.sleep(10)

# This creates orphan process, when parent process executes, and closes,
# The child will become an orphan process. Those processes don't live
# in system on their own, because if so then there won't be any who will
# take their pid, os.wait() and close them. They automatically become inherited by
# init (or systemd) which is the 1 process.

# run ps -C python3 -o pid, ppid, cmd first after running this script, and 10
# seconds later, you'll see that child's process no longer inherited by its parent,
# but the root init process.
