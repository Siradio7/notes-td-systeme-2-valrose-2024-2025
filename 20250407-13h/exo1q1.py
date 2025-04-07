import os, sys
fd1 = os.open("toto.txt", os.O_RDONLY)
print(fd1) # 3
os.close(fd1)
fd2 = os.open("titi.txt", os.O_RDONLY)
print(fd2) # 3
fd3 = os.open("titi.txt", os.O_RDONLY)
print(fd3) # 4
os.close(fd2)
os.close(fd3)
sys.exit(0)