import os, sys
fd1 = os.open("toto.txt", os.O_RDONLY)
bytes_sequence = os.read(fd1, 2) # séquence d'octets
print(bytes_sequence)
print(bytes_sequence.decode("utf-8"))
bytes_sequence = os.read(fd1, 1)
os.close(fd1)
print(bytes_sequence)
print(bytes_sequence.decode("utf-8"))
sys.exit(0)