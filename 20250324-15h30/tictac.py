import time, signal, sys

def handler(_signum, _frame):
    if input("arrêter ? (o/n)") == "o":
        print("bye")
        sys.exit(0)

signal.signal(signal.SIGINT, handler)
while True:
    print("tic")
    time.sleep(1)
    print("tac")
    time.sleep(1)