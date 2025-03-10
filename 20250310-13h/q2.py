#!/usr/bin/env python3
# ligne du dessus = shebang
# rend le programme executable
import os, sys

os.fork()
print("Hello World!")
sys.exit(0)