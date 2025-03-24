# La primitive time.sleep(t) suspend le processus appelant pendant t secondes ou
# jusqu’à l’arrivée d’un signal.
# Écrire un programme qui suspend le processus pendant t secondes passé en paramètre, 
# et aﬃche le message « interruption » en cas d’interruption par Ctrl + C .

import signal, time, sys

t = int(sys.argv[1])

# solution 1: on utilise le fait que l'arrivée du signal SIGINT lève une exception (spécifique à Python) 
# try:
#     time.sleep(t)
# except KeyboardInterrupt:
#     print("interruption")

# solution 2: on utilise un gestionnaire de signal
def my_handler(_signum, _frame):
    print("interruption")
    sys.exit(0)

signal.signal(signal.SIGINT, my_handler)
time.sleep(t)