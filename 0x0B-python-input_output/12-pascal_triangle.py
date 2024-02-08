#!/usr/bin/python3
''' A Python Module '''


def pascal_triangle(n):
    ''' Returns a list of lists of integers '''

    if (n <= 0):
        return []

    result = []

    for x in range(n):
        row = [1]
        if x > 0:
            prev_row = result[-1]
            for y in range(1, x):
                row.append(prev_row[y - 1] + prev_row[y])
            row.append(1)
        result.append(row)

    return result
