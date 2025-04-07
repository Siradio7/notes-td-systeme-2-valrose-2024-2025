import os, sys
# on ouvre un fichier en écriture, s'il n'existe pas, il est créé
fd1 = os.open('tutu.txt', os.O_WRONLY | os.O_CREAT)

print(fd1) # -> 3, premier emplacement libre
print("erreur", file=sys.stderr)

os.close(2)
fd912828 = os.dup(fd1)  # <- cherche un emplacement libre et y copie fd1

# ces deux lignes sont équivalentes
# os.dup2(fd1, 2)

print(fd912828) # -> 2, premier emplacement libre (3 est occupé par fd1)
print("blab lakahskjh", file=sys.stderr) # -> va dans tutu.txt