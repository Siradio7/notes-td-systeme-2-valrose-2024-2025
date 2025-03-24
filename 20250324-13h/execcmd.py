#!/usr/bin/env python3
# le shebang (ligne au-dessus)
# Écrire un programme execcmd.py qui exécute une commande Unix qu’on lui passe en
# paramètre. Exemple d’exécution :
# ./execcmd.py /bin/ls -Ft /
import os, sys
print(f"[depuis execcmd] {os.getpid()}")
chemin_absolu_fichier = sys.argv[1] #"/bin/ls"
argv_utile = sys.argv[1:] #["/bin/ls", "-Ft", "/"]
os.execvp(chemin_absolu_fichier, argv_utile)

# si je veux faire croire au programme que je suis toto
#env = os.environ.copy()
#env['USER'] = 'toto'  # <- en ligne de commande, on ferait `export USER=toto`
#os.execvpe(chemin_absolu_fichier, argv_utile, env)