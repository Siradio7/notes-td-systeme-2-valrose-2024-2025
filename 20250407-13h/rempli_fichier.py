# permet à l'utilisateur de saisir le contenu d'un fichier
# et de le sauvegarder dans un fichier texte

import os, sys
filename = sys.argv[1]
fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
while True:
    c = os.read(0, 1) # on lit un caractère sur l'entrée standard
    if len(c) == 0:
        break
    os.write(fd, c) # on écrit le caractère dans le fichier
os.close(fd) # on ferme le fichier