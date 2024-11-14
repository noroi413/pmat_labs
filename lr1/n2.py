#!/usr/bin/env python3
import random
import sys

def main():
    try:
        A = float(sys.stdin.readline())
        B = random.randint(-10, 10)
        result = A / B
        print(result)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()