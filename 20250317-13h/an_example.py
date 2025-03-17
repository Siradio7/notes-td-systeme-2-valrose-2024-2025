# let's call fork() and see what happens
import os
pid_of_child = os.fork()
if pid_of_child == 0:
    print("I am the child process, my PID is", os.getpid())
else:
    print("I am the parent process, my son's PID is", pid_of_child)