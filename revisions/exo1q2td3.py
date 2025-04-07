import signal, time

def handler(signum, frame):
    print("bip")
    # on programme l'alarme pour 2 secondes
    signal.alarm(2)


# on attache le gestionnaire de signal à SIGALRM
signal.signal(signal.SIGALRM, handler)

# on programme l'alarme pour 2 secondes
signal.alarm(2)

# boucle infinie où il ne se passe rien
# while True:
#     signal.pause()
time.sleep(100)