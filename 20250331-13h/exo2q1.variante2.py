# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. 
#    Le fils envoie le signal SIGUSR1 au père. À la réception du signal, le père 
#    affiche un message puis envoie le signal SIGUSR1 au fils. 
#    À la réception du signal, le fils affiche un message puis se termine. 
#    Le père attend la fin du fils, affiche un message puis se termine.

# contrainte supplémentaire: le handler ne fait pas de `if``

import os, signal, sys, time

def handler_du_pere(signum, _frame):
    global pid_du_fils
    print(f"Signal {signum} reçu par {os.getpid()}")
    os.kill(pid_du_fils, signal.SIGUSR1)

def handler_du_fils(signum, _frame):
    print(f"Signal {signum} reçu par {os.getpid()}")

signal.signal(signal.SIGUSR1, handler_du_pere)

pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    signal.signal(signal.SIGUSR1, handler_du_fils)
    pid_du_pere = os.getppid()
    os.kill(pid_du_pere, signal.SIGUSR1)
    signal.pause()  # Attendre le signal SIGUSR2
    sys.exit(0)

# père
os.wait()