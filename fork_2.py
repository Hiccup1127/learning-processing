import os
import sys
import time

pid = os.fork()


if (pid == 0):
	a = input(f"[Child {os.getpid()}] type in here ^^ -> ")
	print("hello from child")
	time.sleep(2)

	print("[Child {os.getpid()}] exiting")
	sys.exit(0)

else:
	a = input(f"[Parent {os.getpid()}] type smth -> ")
	print("hello from parent")
	time.sleep(5)

	print(os.wait())
	print(pid) # the same as the first number of wait - child' pid
