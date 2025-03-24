#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Écrire un programme verifier.py dont l’usage sera
# ./verifier.py com arg1 .. argn
# et qui lance la commande com arg1 .. argn, signale une éventuelle erreur lors du lancement, attend la fin de l’exécution et précise par un message le résultat (succès ou échec).

import os, sys

# message d'usage
usage = "Usage: verifier.py com arg1 .. argn"

com = sys.argv[1]
argv_utile = sys.argv[1:]
pid_de_mon_fils = os.fork()
if pid_de_mon_fils == 0:
    # le fils
    try:
        os.execvp(com, argv_utile)
    except:
        print(f"Erreur lors du lancement de la commande {com}")
        sys.exit(1)
# le parent
_pid, status = os.wait()
if os.WIFEXITED(status) and os.WEXITSTATUS(status) == 0:
    print("Succès de la commande")
else:
    print("Échec de la commande")
sys.exit(0) # <- pas nécessaire, mais pour la clarté, implicite