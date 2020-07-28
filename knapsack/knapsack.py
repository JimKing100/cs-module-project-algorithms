#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


# Knapsack problem solver returning maximum value and list of items
def knapsack_solver(items, capacity):
    # Initialize n and 2D array
    n = len(items)
    twod_array = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    # Build 2D table with columns set to capacity and rows set to size
    # Each entry will be filled with the maximum j-size for 1 to i-row
    for i in range(n + 1):
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                twod_array[i][c] = 0
            elif items[i-1].size <= c:
                twod_array[i][c] = max(items[i-1].value +
                                       twod_array[i-1][c-items[i-1].size],
                                       twod_array[i-1][c])
            else:
                twod_array[i][c] = twod_array[i-1][c]

    # Store the items which are placed in the knapsack
    new_array = []
    final = twod_array[n][capacity]
    c = capacity

    # Working backwords, the the result is from one of the
    # two max values as above, if not twod_array[i-1][c] then
    # include the item.
    for i in range(n, 0, -1):
        if final <= 0:
            break
        if final == twod_array[i-1][c]:
            continue
        else:
            # The item is included
            new_array.append(items[i-1].index)
            # Size is included so deduct its value
            final -= items[i-1].value
            c -= items[i-1].size

    # Create the results dictionary
    results = {'Value': twod_array[n][capacity], 'Chosen': sorted(new_array)}

    return results


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()

        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
