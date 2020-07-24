#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    base = [['rock'], ['paper'], ['scissors']]
    if n <= 0:
        return [[]]
    if n == 1:
        result = base
        return result
    else:
        arr = []
        for i in range(3**(n-1)):
            for j in range(3):
                prev = rock_paper_scissors(n-1)
                arr.append(prev[i] + base[j])
        result = arr
        return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
