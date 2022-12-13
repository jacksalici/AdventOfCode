from collections import deque
import sys


heightsMap=[]
minpath=9999999

def neighbors(r,c):
    global heightsMap
    #idea from https://github.com/mebeim/aoc/blob/master/2022/README.md#day-12---hill-climbing-algorithm
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if 0 <= nr < len(heightsMap) and 0 <= nc < len(heightsMap[0]): 
            if heightsMap[nr][nc] <= heightsMap[r][c] + 1:  
                yield [nr, nc]

def bfs(r, c, re, ce):
    visited=[]
    queue = deque([(0,[r,c])])

    while queue:
        distance, rc = queue.popleft()

        if (rc == [re, ce]):
            return distance

        if  rc not in visited:
            visited+=[rc]
            

            for neighbor in neighbors(rc[0],rc[1]):
                if neighbor not in visited:
                    queue.append([(distance+1),neighbor])

    return 9999999


with open(sys.argv[1], "rb") as file:
    #READING
    lines = file.read().splitlines()
    heightsMap = list(map(list, lines))

    #CALC
    for r in range(0,len(heightsMap)):
        for c in range(0,len(heightsMap[0])):
            if heightsMap[r][c]==ord('S'):
                heightsMap[r][c]=ord('a')
                rStart, cStart=r,c
            if heightsMap[r][c]==ord('E'):
                rEnd, cEnd=r,c
                heightsMap[r][c]=ord('z')
    
    minpath = bfs(rStart, cStart, rEnd, cEnd)

print (minpath)
        
            
