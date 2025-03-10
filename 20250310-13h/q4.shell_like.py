import os, sys, time, random
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
affiche()
for _ in range(n):
    if os.fork() == 0:
        # si on veut observer le parallelisme entre les fils 
        #time.sleep(random.randint(1, 5))
        affiche()
        sys.exit(0)
    