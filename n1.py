#!/usr/bin/env python3
import random
import sys

def main():
    try:
        A = random.randint(-10, 10)
        print(A)
    except Exception as e:
       print(f"error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()