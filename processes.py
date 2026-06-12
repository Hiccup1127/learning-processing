import signal
import ctypes
import os
import time

# ---- This runs sleeping process (S) - it waits for action ----
#a = input()

# ---- This runs just Runnable process (R) ----
#while (True): print(1)

# ---- This process will be stopped(T) if press Ctrl+Z ----
#time.sleep(3)

# ---- This runs Runnable process(R) that couldn't be cilled by terminating ----
#signal.signal(signal.SIGINT, signal.SIG_IGN)
#signal.signal(signal.SIGTERM, signal.SIG_IGN)
#
#while (True): print(1)

# ---- This runs stopped process(T or t flag) ----
#libc = ctypes.CDLL("libc.so.6")
#ptrace_traceme = 0
#
#print(f"pid-{os.getpid()}")
#print("Request")
#
#libc.ptrace(ptrace_traceme, 0, 0, 0)
#
#os.kill(os.getpid(), 5)
#
#while (True): print("under trace!!!"); time.sleep(1)

# ---- This runs a Zombie process (Z), actually, an ended child process ----
#pid = os.fork()
#if (pid == 0):
#	print("I\'m a child process! my pid: %i" % os.getpid())
#else:
#	while (True): print(1)
