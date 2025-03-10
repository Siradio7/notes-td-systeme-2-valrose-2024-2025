# coding: utf-8
import os, sys
x = 1
mon_pid = os.fork()
if mon_pid == 0: # child
    x = x + 1
    print("child: x =", x)
    sys.exit(11)
# parent
x = x - 1
print("parent: x =", x)
sys.exit(0)