import os
if os.fork() == 0:
    # fils = producteur
    fd_out = os.open("montube", os.O_WRONLY)
    for i in range(26):
        c = chr(97 + i)
        os.write(fd_out, c.encode())
    os.close(fd_out)

# pere = consommateur
fd_in = os.open("montube", os.O_RDONLY)
while True:
    c = os.read(fd_in, 1)
    if len(c) == 0:
        break
    print(c.decode(), end="")
os.close(fd_in)