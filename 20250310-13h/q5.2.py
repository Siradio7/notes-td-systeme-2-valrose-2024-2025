import os, sys, time, random

def affiche():
    mon_pid = os.getpid()
    pid_de_mon_pere = os.getppid()
    print(f"{mon_pid=}, {pid_de_mon_pere=}")

affiche()
if not os.fork() : # fils ## `not os.fork()` équivaut à `os.fork() == 0`
    affiche()
    pid = os.fork()
    if not os.fork(): # petit-fils 
        affiche()
        sys.exit(0)
    sys.exit(0)
sys.exit(0) # pere
