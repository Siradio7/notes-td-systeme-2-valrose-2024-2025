# Lorsqu’un processus crée des processus fils, il peut attendre 
# leur fin avec la primitive `os.wait` ou `os.waitpid`. 
# Néanmoins, il ne peut pas faire de travail utile pendant
# cette attente. C’est pourquoi on souhaite que le processus père 
# traite la fin de ses fils uniquement au moment où cette fin est 
# signalée par le signal SIGCHLD.

# Écrire le programme d’un processus créant plusieurs fils et traitant 
# leur fin comme il vient d’être indiqué.

import os, signal, sys, time, random

nb_fils = 10
c=0
def handler(_signum, _frame):
    global c
    print(f"[pere] SIGCHLD reçu, {c=}")
    while True:
        pid, _status = os.waitpid(0, os.WNOHANG) 
        if pid == 0 : # attend la fin d'un fils
            break
        c += 1
        if c == nb_fils:
            print("bye")
            sys.exit(0)

signal.signal(signal.SIGCHLD, handler)  # régler le handler avant le fork


# création des fils, chacun d'eux va dormir entre 1 et 3 secondes
for i in range(nb_fils):
    pid = os.fork()
    if pid == 0:
        # le fils
        time.sleep(random.randint(1, 3))  # simule un travail
        sys.exit(0)

# le père
while True:
    print("[pere] tic")
    time.sleep(1)  # simule un travail
    print("[pere] tac")
    time.sleep(1)  # simule un travail