# ecrit l'alphabet caractere par caractere dans un fichier alphabet.txt
# en utilisant os.open et os.write et os.close
import os

# on ouvre le fichier en mode ecriture, s'il n'existe pas, on le cree
# s'il existe, on le tronque au début
fd = os.open("alphabet.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)


# on ecrit l'alphabet caractere par caractere
for i in range(26):
    # on ecrit le caractere correspondant
    c = chr(i + 97)
    os.write(fd, c.encode())

# on ferme le fichier
os.close(fd)