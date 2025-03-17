import os, sys, time
print("Hello")
pid = os.fork()
print("ici : {}".format(pid))
if pid != 0: # Parent
    pid_wait, status = os.waitpid(-1, 0)
    if os.WIFEXITED(status):
        print("là : {}".format(os.WEXITSTATUS(status)))
    print("Bye")
    sys.exit(2)
#time.sleep(100)# si on veut pouvoir tuer le fils avec `kill -9`
sys.exit(0)