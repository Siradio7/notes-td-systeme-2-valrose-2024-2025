import os
argv = ["ls", "-lt", "/"]
os.execv("/bin/ls", argv)
# équivalent à taper directement dans le terminal
# `ls -lt /`