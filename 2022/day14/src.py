from itertools import tee
from pprint import pprint
import sys


materialMap=[['.' for i in range (1000)] for j in range(1000)]

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)



with open(sys.argv[1], "r") as file:
    for line in file.readlines():
        for pair in pairwise(line.strip().split(" -> ")):
            a, b = pair
            a, b = a.split(','), b.split(',')
            for i in range (2):
                if a[i] == b[i]:
                    fixed = int(a[i])
                    start, end = int(a[1-i]), int(b[1-i])+1
                    for j in range (start, end):
                        if i: #i = 1, col is fixed
                            materialMap[j][fixed] = '#'
                        else:
                            materialMap[fixed][j] = '#'
    
    for line in materialMap[0:300]:
        print(*line[300:700])