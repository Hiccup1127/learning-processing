import threading
import time

def sum(a, b):
	time.sleep(3)
	print(a+b)

def sub(a, b):
	time.sleep(2)
	print(a-b)

thread1 = threading.Thread(target=sum, args=(3, 5))
thread2 = threading.Thread(target=sub, args=(5, 4))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Thread - A thread is the smallest unit of execution that an
# operating system can schedule. It is often called a lightweight process.

# While a process represents the container (the memory, the network
# sockets, the file handles), the thread represents the actual
# execution (running the code). Every single process has at least one
# thread — the "main thread", but it can spawn many more.
