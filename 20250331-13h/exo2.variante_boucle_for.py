# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. 
#    Le fils envoie le signal SIGUSR1 au père. À la réception du signal, le père 
#    affiche un message puis envoie le signal SIGUSR2 au fils. 
#    À la réception du signal, le fils affiche un message puis se termine. 
#    Le père attend la fin du fils, affiche un message puis se termine.
# 2. Modifier le programme pour qu'il reçoive un entier n sur la ligne de commande,
#    et modifier le fils et le père pour que l'échange de signaux se passe 
#    successivement n fois.

import os, signal, sys, time

n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Entrez un entier n: "))

nb_signaux_recus = 0  # <- variable globale pour le nombre de signaux reçus par le processus qui possède cette copie de la variable

def handler_du_pere_et_du_fils(signum, _frame):
    global pid_du_fils, nb_signaux_recus
    nb_signaux_recus += 1
    print(f"nombre de signaux reçus: {nb_signaux_recus} par {os.getpid()}")
    print(f"Signal {signum} reçu par {os.getpid()}")
    #if pid_du_fils !=0:
    # ou bien
    if signum == signal.SIGUSR1:
        # je suis le père
        os.kill(pid_du_fils, signal.SIGUSR2)
    else:
        # je suis le fils
        if nb_signaux_recus < n:
            os.kill(os.getppid(), signal.SIGUSR1)

signal.signal(signal.SIGUSR1, handler_du_pere_et_du_fils)
signal.signal(signal.SIGUSR2, handler_du_pere_et_du_fils)

pid_du_fils = os.fork()
if pid_du_fils == 0:
    # fils
    pid_du_pere = os.getppid()
    os.kill(pid_du_pere, signal.SIGUSR1)
    for _ in range(n): # de manière répétée, à l'infini
        signal.pause()  # Attendre le signal SIGUSR2 (1 fois) 
    sys.exit(0)

# père
os.wait()
sys.exit(0) # <- implicite