#!/usr/bin/env python3
# le shebang (ligne au-dessus)
# Écrire un programme execcmd.py qui exécute une commande Unix qu’on lui passe en
# paramètre. Exemple d’exécution :
# ./execcmd.py /bin/ls -Ft /
import os, sys

# enlever le commentaire pour observer que le pid ne change pas entre ce programme et celui exécuté
# ./execmd.py print_pid.py
#print(f"[depuis execcmd] {os.getpid()}")

# on recupere le nom de la commande et ses arguments
try :
    chemin_absolu_fichier = sys.argv[1] #"/bin/ls"
    argv_utile = sys.argv[1:] #["/bin/ls", "-Ft", "/"]
except:
    print("Usage: execcmd.py /bin/ls -Ft /")
    sys.exit(1)

#os.execvp(chemin_absolu_fichier, argv_utile)
# mieux: on autorise aussi à avoir le nom de l'executable sans le chemin (on cherche dans le PATH)
os.execvp(chemin_absolu_fichier, argv_utile)

# si je veux faire croire au programme que je suis toto
#env = os.environ.copy()
#env['USER'] = 'toto'  # <- en ligne de commande, on ferait `export USER=toto`
#os.execvpe(chemin_absolu_fichier, argv_utile, env)