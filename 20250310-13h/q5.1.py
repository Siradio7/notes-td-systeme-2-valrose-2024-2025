import os, sys, time, random

def affiche():
    mon_pid = os.getpid()
    pid_de_mon_pere = os.getppid()
    print(f"{mon_pid=}, {pid_de_mon_pere=}")

affiche()
pid = os.fork()
if pid == 0: # fils 1
    affiche()
    sys.exit(0)
pid = os.fork()
if pid == 0: # fils 2
    affiche()
    sys.exit(0)
# implicite
#sys.exit(0) # pere