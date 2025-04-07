# print hello après avoir redirigé la sortie
# standard vers un fichier

import os

# os.close(1) # <- ferme la sortie standard
# fd = os.open("hello.txt", os.O_WRONLY | os.O_CREAT)
# fd = 1

# ou bien
fd = os.open("hello.txt", os.O_WRONLY | os.O_CREAT)
os.dup2(fd, 1) # redirige la sortie standard vers le fichier

print("hello")