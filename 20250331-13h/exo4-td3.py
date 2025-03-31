# pour tester le programme, un exemple:
# python3 exo4-td3.py ls exo1.py --then echo succes --else echo echec --fi

import sys, os
index_then = sys.argv.index("--then")
index_else = sys.argv.index("--else")
index_fin = sys.argv.index("--fi")
arguments_cmd1 = sys.argv[1:index_then]
arguments_cmd2 = sys.argv[index_then + 1:index_else]
arguments_cmd3 = sys.argv[index_else + 1:index_fin]

pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    os.execvp(arguments_cmd1[0], arguments_cmd1)
    assert(False) # <- on n'arrive jamais ici

# père
_pid, status = os.waitpid(pid_du_fils, 0)
if os.WIFEXITED(status):
    # le fils s'est terminé normalement
    if os.WEXITSTATUS(status) == 0:
        # le fils s'est terminé avec succès
        os.execvp(arguments_cmd2[0], arguments_cmd2)
    else:
        # le fils s'est terminé avec une erreur
        os.execvp(arguments_cmd3[0], arguments_cmd3)