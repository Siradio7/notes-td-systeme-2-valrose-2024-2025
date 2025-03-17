# question 1: afficher les processus dans leur ordre de création
# première solution: on spécifie quel processus attendre
import errno, os, sys
nbChildren = 20

# la liste des pids des enfants
pids = []

for i in range(nbChildren):
    pid = os.fork()
    if pid == 0: # child
        sys.exit(100 + i)
    else: # parent
        pids.append(pid)

print(f"{pids=}")

for pid in pids:
    print(f"waiting for child {pid} to terminate")
    _pid, status = os.waitpid(pid, 0)
    # _pid == pid
    if os.WIFEXITED(status):
        print(f"child {pid} terminated normally with exit status={os.WEXITSTATUS(status)}")
    else:
        print("child {} terminated abnormally".format(pid))

print("No more children left. Bye", file=sys.stderr)
sys.exit(0)