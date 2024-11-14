#!/usr/bin/env python3
import math
import sys

def main():
    try:
        a = float(sys.stdin.readline())
        result = math.sqrt(a)
        with open('output.txt', 'w') as output_file:
            output_file.write(f'{result}\n')
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()