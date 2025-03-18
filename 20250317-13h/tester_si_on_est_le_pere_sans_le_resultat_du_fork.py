import os
pid1 = os.getpid()
os.fork()
pid2 = os.getpid()
if pid1 == pid2:
    print("Je suis le père")
else:
    print("Je suis le fils")