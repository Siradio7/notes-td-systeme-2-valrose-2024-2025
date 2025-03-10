#!/usr/bin/env python3
# ligne du dessus = shebang
# ajouter ça et donner les droits en exécution sur le fichier
# avec `chmod u+x q2.py` 
# fait de ce fichier un exécutable
# pour tester: `./q2.py` depuis un terminal
import os, sys

os.fork()
print("Hello World!")
sys.exit(0)
