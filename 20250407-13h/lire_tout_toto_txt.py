# on veut lire tout le fichier toto.txt et l'afficher
# en utilisant os.read()
import os
fd = os.open("toto.txt", os.O_RDONLY)
acc = b''
while True:
    buf = os.read(fd, 5)
    print(len(buf))
    if len(buf) == 0:
        break
    acc += buf
os.close(fd)
print(acc.decode('utf-8'))