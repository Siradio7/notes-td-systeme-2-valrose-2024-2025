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

try: # parent waits for all of its children to terminate
    i = 0
    while True:
        print(f"waiting for child {pids[i]} to terminate")
        pid, status = os.waitpid(pids[i], 0)
        # pid == pids[i] car on attend un processus à la fois
        i += 1
        if os.WIFEXITED(status):
            print(f"child {pid} terminated normally with exit status={os.WEXITSTATUS(status)}")
        else:
            print("child {} terminated abnormally".format(pid))

except OSError as e:
    print(f"waitpid error: {errno.errorcode[e.errno]}, {os.strerror(e.errno)}", file=sys.stderr)
    if e.errno == errno.ECHILD:
        print("No more children left. Bye", file=sys.stderr)
        sys.exit(0)