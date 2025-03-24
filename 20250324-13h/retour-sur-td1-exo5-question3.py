import os, time, sys, signal

def handler(_signum, _frame):
    print("bye")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
while True:
    PID = os.getpid()
    print(f"PID: {PID}")
    time.sleep(10) # <- dans l'enonce 2 secondes
    pid_of_my_son = os.fork()
    if pid_of_my_son != 0:
        # le parent
        sys.exit(0)
