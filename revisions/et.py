# fait l'équivalent de `command1 && command2` dans le shell
# usage: et <command1> <command2>

import os, sys
pid_fils = os.fork()
if pid_fils == 0:
    # fils
    try:
        os.execvp(sys.argv[1], sys.argv[1:2])
    except:
        # si la commande échoue, on sort du fils
        sys.exit(1)

# père: on attend la fin du fils et on vérifie son code de sortie
_pid, status = os.wait()
if not os.WIFEXITED(status): # si le fils a été tué par un signal, on sort
    sys.exit(1)
if os.WEXITSTATUS(status) != 0: # si le code de sortie n'est pas 0, on sort
    sys.exit(1)
# sinon la premiere commande a réussi, on lance la deuxième    
pid_fils = os.fork()
if pid_fils == 0:
    # fils
    try:
        os.execvp(sys.argv[2], sys.argv[2:])
    except:
        # si la commande échoue, on sort du fils
        sys.exit(1)
# père
_pid, status = os.wait()
if not os.WIFEXITED(status):
    sys.exit(1)
if os.WEXITSTATUS(status) != 0:
    sys.exit(1)
# sinon la deuxième commande a réussi, on sort avec le code de sortie 0
sys.exit(0)