import sys, os
print(sys.argv)

if len(sys.argv) == 1:
    print("Usage: python execcmd.py <command> [args]")
    sys.exit(1) # <- signale une erreur

os.execvp(sys.argv[1], sys.argv[1:])
