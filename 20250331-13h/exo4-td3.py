# pour tester le programme, un exemple:
# python3 exo4-td3.py ls exo1.py --then echo succes --else echo echec --fi

import sys, os
index_then = sys.argv.index("--then")
index_else = sys.argv.index("--else")
index_fin = sys.argv.index("--fi")
arguments_cmd1 = sys.argv[1:index_then]
arguments_cmd2 = sys.argv[index_then + 1:index_else]
arguments_cmd3 = sys.argv[index_else + 1:index_fin]

def exec_cmd(argv):
    # une surcouche à os.execvp qui 
    # rattrape un recouvrement un cas d'échec
    try:
        os.execvp(argv[0], argv)
    except:
        print(f"Erreur: commande {argv[0]} introuvable")
        sys.exit(1)  # <- pour indiquer qu'il y a eu une erreur


pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    exec_cmd(arguments_cmd1)
    assert(False) # <- pédagogique, pour indiquer que cette ligne est inatteignable; inutile sinon
    

# père
_pid, status = os.waitpid(pid_du_fils, 0)
if os.WIFEXITED(status):
    # le fils s'est terminé normalement
    if os.WEXITSTATUS(status) == 0:
        # le fils s'est terminé avec succès
        exec_cmd(arguments_cmd2)
        assert(False) 
    else:
        # le fils s'est terminé avec une erreur
        exec_cmd(arguments_cmd3)
        assert(False) 
