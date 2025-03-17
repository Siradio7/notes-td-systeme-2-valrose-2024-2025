import errno, os, sys
nbChildren = 20
for i in range(nbChildren):
    pid = os.fork()
    if pid == 0: # child
        sys.exit(100 + i)
    _pid, status = os.wait() # équivalent à waitpid(-1, 0)
    # _pid == pid
    if os.WIFEXITED(status):
        print(f"child {_pid} terminated normally with exit status={os.WEXITSTATUS(status)}")
    else:
        print("child {} terminated abnormally".format(_pid))

print("No more children left. Bye", file=sys.stderr)
sys.exit(0)