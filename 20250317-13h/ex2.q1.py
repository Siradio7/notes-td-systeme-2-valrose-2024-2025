import os, sys, time
print(f"{os.getpid()}")
pid_de_mon_fils = os.fork()
if pid_de_mon_fils == 0:
    # Je suis le fils
    print(f"{os.getpid()}")
    time.sleep(5)
    sys.exit(0)
# Je suis le père
print(f"{pid_de_mon_fils=}")
os.waitpid(pid_de_mon_fils, 0)
# ou simplement os.wait()
print("Le fils est mort")
