# coding: utf-8
# ligne de dessus optionnelle, permet de spécifier l'encodage du fichier (par défaut utf-8)
# pour exécuter ce fichier depuis un terminal
# 1. se placer dans le bon répertoire (commande `cd`)
# 2. taper `python q1.py`
import os, sys
x = 1
mon_pid = os.fork()
if mon_pid == 0: # child
    x = x + 1
    print("child: x =", x)
    sys.exit(11)
# parent
x = x - 1
print("parent: x =", x)
sys.exit(0)
