# La primitive signal.alarm(t) provoque l’envoi d’un signal signal.SIGALRM au
# processus appelant au bout de t secondes. Attention : les programmations 
# successives d’alarmes ne sont pas empilées, chaque appel de alarm annule 
# l’éventuelle programmation précédente.

# Écrire un programme qui ne fait rien (exécute une boucle vide) mais qui 
# reçoit un signal signal.SIGALRM toutes les secondes, et aﬃche alors un 
# message «bip». À la réception du sixième signal, le programme aﬃche « bye » et 
# se termine.

import signal, time, sys

t = int(sys.argv[1])

# exemple plus simple d'utilisation de signal.alarm
# def handler(_signum, _frame):
#     print("signal SIGALRM reçu")
#     sys.exit(0)

# signal.signal(signal.SIGALRM, handler)
# signal.alarm(10)  # programme l'envoi du signal SIGALRM dans 10 secondes
# while True:
#     pass

def handler(_signum, _frame):
    global count
    count += 1
    print("bip")
    if count == 6:
        print("bye")
        sys.exit(0)
    signal.alarm(t)  # programme l'envoi du prochain signal SIGALRM dans t secondes
    # dans t secondes, s'appelera "recursivement"


count = 0
signal.signal(signal.SIGALRM, handler)
signal.alarm(t)  # programme l'envoi du premier signal SIGALRM dans t secondes

while True:
    pass


