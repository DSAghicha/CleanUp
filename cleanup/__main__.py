import sys
import os
from cleanup import cleanup


def main():
    print("CleanUP v1.0")
    commands = sys.argv[1:]
    if len(commands) == 0:
        info()
    else:
        for command in commands:
            if command == "-h":
                info()
            elif command == ".":
                curr_dir = os.getcwd()
                cleanup.cleanup(curr_dir)
            elif command == "-f":
                working_dir = " ".join(commands[1:])
                print(working_dir)
                cleanup.cleanup(working_dir)


def info():
    print(''"Usage:-")
    print("-h{}: Show usage".format(" " * (15 - len("-h"))))
    print(".{}: Run CleanUP in the current directory!".format(" " * (15 - len("."))))
    print("-f 'file path'{}: Run CleanUP in the given directory".format(" " * (15 - len("-f 'file path'"))))
    print("-i{}: See Tool Info".format(" " * (15 - len("-i"))))


if __name__ == '__main__':
    main()
