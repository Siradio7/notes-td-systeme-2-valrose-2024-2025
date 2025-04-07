# usage : timeout.py t cmd
# lance la commande cmd et l'arrête après t secondes si elle n'est pas terminée
import os, signal, sys

def handler(signum, frame):
    os.kill(pid_fils, signal.SIGKILL)

cmd = sys.argv[2]
args = sys.argv[2:]
pid_fils = os.fork()
if pid_fils == 0:
    os.execvp(cmd, args)

# le père attend la fin du fils, mais pas plus de t secondes. Comment?
# 1. on attache un handler au signal SIGALRM
signal.signal(signal.SIGALRM, handler)
# 2. on lance le timer
t = int(sys.argv[1])
signal.alarm(t)
# 3. on attend la fin du fils (mais peut-être SIGALRM arrivera avant)
os.wait()