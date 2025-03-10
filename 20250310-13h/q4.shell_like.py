import os, sys, time, random

try:
    n = int(sys.argv[1])
except:
    print("Usage: python3 q4.escalier.py <n>")
    sys.exit(1)
def affiche():
    mon_pid = os.getpid()
    pid_de_mon_pere = os.getppid()
    print(f"{mon_pid=}, {pid_de_mon_pere=}")

affiche()

for _ in range(n):
    if os.fork() == 0:
        # décommenter la ligne ci-dessous pour observer le parallelisme entre les différents processus
        #time.sleep(random.randint(1, 5))
        affiche()
        sys.exit(0)
    
