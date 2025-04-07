import os
# provoque un interblocage
# illustre le fait que open d'un tube est bloquant (sémantique de rendez-vous)

# producteur
fd_out = os.open("montube", os.O_WRONLY) # <- bloquant!
for i in range(26):
    c = chr(97 + i)
    os.write(fd_out, c.encode())
os.close(fd_out)

# consommateur
fd_in = os.open("montube", os.O_RDONLY)
while True:
    c = os.read(fd_in, 1)
    if len(c) == 0:
        break
    print(c.decode(), end="")
os.close(fd_in)