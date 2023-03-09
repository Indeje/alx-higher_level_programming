#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = 1
    if len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments.")
    elif len(sys.argv) == 2:
        print(f"{len(sys.argv) - 1} argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    args = sys.argv
    args.pop(0)
    for arg in args:
        print(f"{count}: {arg}")
        count += 1
