import os, time, sys
while True:
    PID = os.getpid()
    print(f"PID: {PID}")
    time.sleep(10) # <- dans l'enonce 2 secondes
    pid_of_my_son = os.fork()
    if pid_of_my_son != 0:
        # le parent
        sys.exit(0)
