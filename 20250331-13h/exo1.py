# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. 
#    Le fils envoie le signal SIGUSR1 au père puis se termine.
# 2. Modifier le père pour qu'il affiche un message lorsque le signal SIGUSR1 est 
#    capté.
# 3. Modifier le programme pour qu'il reçoive un entier n sur la ligne de commande, et
#    modifier le fils de telle sorte qu'il envoie à la suite n signaux SIGUSR1 au père 
#    avant de se terminer.
# 4. Modifier le père pour qu'il compte le nombre de signaux SIGUSR1 reçus ; supprimer
#    tout affichage dans le handler de signal du père, et afficher le nombre de signaux
#    reçus après la fin du fils.

import os, signal, sys, time

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nb_signaux = 0

def handler(signum, _frame):
    #print(f"Signal {signum} reçu") # <- à supprimer à la question 4
    global nb_signaux
    nb_signaux += 1

signal.signal(signal.SIGUSR1, handler)

pid_du_fils = os.fork()

if pid_du_fils == 0 :
    # fils
    pid_du_pere = os.getppid()
    for _ in range(n):
        #time.sleep(1)  # Simule un travail
        os.kill(pid_du_pere, signal.SIGUSR1)
    sys.exit(0)  # <- important pour que le fils ne "sorte pas du if"

# père
#os.wait() 
# ou de manière équivalente
_pid, _status = os.waitpid(pid_du_fils, 0)
print("nombre de signaux reçus:", nb_signaux)
print("bye")