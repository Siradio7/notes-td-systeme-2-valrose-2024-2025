import os, time, sys, signal
while True:
    PID = os.getpid()
    print(f"PID: {PID}")
    time.sleep(10) # <- dans l'enonce 2 secondes
    pid_of_my_son = os.fork()
    if pid_of_my_son != 0:
        # le parent
        sys.exit(0)


# pour tuer le processus depuis le terminal
# kill -SIGINT <PID>
# ou plus court
# kill -9 <PID>
# avec PID le dernier PID affiché