import os
(fd_in, fd_out) = os.pipe()
for i in range(26):
    c = chr(i + 97)
    os.write(fd_out, c.encode())
buf = os.read(fd_in, 1024)
print(buf.decode())
os.close(fd_in)
os.close(fd_out)