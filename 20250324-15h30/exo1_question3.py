# (a) Que fait ce programme?

# voir photo

# (b) Quelle est à votre avis la valeur imprimée pour la variable counter ?
# 5

# (c) Voyez-vous un problème potentiel?

# certains signaux peuvent être perdus parce qu'ils arrivent pendant qu'un signal precedent est en cours de traitement

import os, signal, sys, time

counter = 0

def handler(sig, ignore):
    global counter
    counter += 1
    time.sleep(0.1) # simuler du travail pour le handler


def parent():
    try:
        os.wait() # attend que le fils se termine
    except:
        pass # ignore l'exception si le fils est déjà mort
    print(f"{counter=}")
    sys.exit(0)

def child():
    for i in range(5):
        os.kill(os.getppid(), signal.SIGUSR2)
        print("send SIGUSR2 to parent")
        #time.sleep(0.2) # pour "eviter" de saturer le parent

    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGUSR2, handler) # régler le handler avant le
    pid = os.fork() # début du fils
    if pid == 0:
        child()
    else:
        parent()