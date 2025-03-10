# coding: utf-8
# ligne de dessus optionnelle, permet de spécifier l'encodage du fichier (par défaut utf-8)
# pour exécuter ce fichier depuis un terminal
# 1. se placer dans le bon répertoire (commande `cd`)
# 2. taper `python q1.py`
# 3. afficher le code de sortie avec `echo $?` (affiche 0, et non pas 11, qui est le code de sortie du fils...)
import os, sys
x = 1
pid_de_mon_fils = os.fork()
if pid_de_mon_fils == 0: # je suis le fils
    x = x + 1
    print("child: x =", x)
    sys.exit(11)
# je suis le père
x = x - 1
print("parent: x =", x)
sys.exit(0)

