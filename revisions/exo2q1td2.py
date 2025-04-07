# Écrire un programme Python qui aﬃche son PID, puis crée un fils. Le père aﬃche
# son PID, puis aﬃche un message signalant que son fils est mort lorsque c’est bien
# le cas. Le fils aﬃche son PID, s’endort 5 secondes puis se termine.

import os, sys, time
mon_pid = os.getpid()
print("mon pid est : ", mon_pid)
pid_fils = os.fork()
if pid_fils == 0:
    # je suis le fils
    print("[fils] mon pid est : ", os.getpid()) # attention, mon_pid est celui du père
    time.sleep(5)
    sys.exit(0)
# père
print("[père] mon pid est : ", mon_pid)
os.wait()
print("[père] mon fils est mort")