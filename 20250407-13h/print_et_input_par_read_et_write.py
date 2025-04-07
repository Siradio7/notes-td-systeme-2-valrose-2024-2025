import os
def print(s):
    byts = s.encode('utf-8')
    for b in byts:
        os.write(1, b)
    os.write(1, b'\n')

def input():
    byts = os.read(0, 1024)
    return byts.decode('utf-8')