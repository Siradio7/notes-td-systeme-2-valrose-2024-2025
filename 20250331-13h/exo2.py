# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. 
#    Le fils envoie le signal SIGUSR1 au père. À la réception du signal, le père 
#    affiche un message puis envoie le signal SIGUSR2 au fils. 
#    À la réception du signal, le fils affiche un message puis se termine. 
#    Le père attend la fin du fils, affiche un message puis se termine.
# 2. Modifier le programme pour qu'il reçoive un entier n sur la ligne de commande,
#    et modifier le fils et le père pour que l'échange de signaux se passe 
#    successivement n fois.


import os, signal, sys, time

def handler_du_pere_et_du_fils(signum, _frame):
    global pid_du_fils
    print(f"Signal {signum} reçu par {os.getpid()}")
    #if pid_du_fils !=0:
    # ou bien
    if signum == signal.SIGUSR1:
        # je suis le père
        os.kill(pid_du_fils, signal.SIGUSR2)

signal.signal(signal.SIGUSR1, handler_du_pere_et_du_fils)
signal.signal(signal.SIGUSR2, handler_du_pere_et_du_fils)

pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    pid_du_pere = os.getppid()
    os.kill(pid_du_pere, signal.SIGUSR1)
    signal.pause()  # Attendre le signal SIGUSR2
    sys.exit(0)

# père
os.wait()