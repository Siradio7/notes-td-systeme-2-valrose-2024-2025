import os, sys
#print(sys.argv)
try:
    n = int(sys.argv[1])
except:
    print("Usage: python3 q4.escalier.py <n>")
    sys.exit(1)
# a vous!
def affiche():
    mon_pid = os.getpid()
    pid_de_mon_pere = os.getppid()
    print(f"{mon_pid=}, {pid_de_mon_pere=}")
for _ in range(n):
    affiche()
    if os.fork() != 0: 
        sys.exit(0)
affiche()