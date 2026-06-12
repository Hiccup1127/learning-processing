import os
import sys
import time

pid = os.fork()

if (pid==0):
	print(f"[Child {os.getpid()}] I'm working haaard...")
	time.sleep(10)

	sys.exit(0)

q = input("Hello! Hope you're doing great? This message runs aside of child process.")

print(f"[Parent {os.getpid()}, child's id: {pid}] Waiting for child...")
os.wait()

a = int(input("Enter a -> "))
b = int(input("Enter b -> "))

print("Result is %i"%(a+b))
