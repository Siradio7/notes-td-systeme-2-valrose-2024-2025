import os

def do_it():
    os.fork()
    os.fork()
    print("Hello World!")

if __name__ == "__main__":
    do_it()
    print("Hello World!")