from pprint import pprint
import sys


mmap=[]
visible=0

def maxHeight(r, c, p):
    #left
    m = 0
    if p == 2:
        m = max(mmap[r][0:c])
    #right
    if p == 0:
        m = max(mmap[r][c+1:])
    
    col = []
    for i in range(0,len(mmap)):
        for j in range(0,len(mmap[0])):
            if j == c:
                col.append(mmap[i][j])
    
    #top
    if p == 1:
        m = max(col[0:r])
    
    if p == 3:
        m = max(col[r+1:])
    
    return m





with open(sys.argv[1], "r") as file:
    #READING
    for i, line in enumerate(file):
        mmap.append([int(c) for c in line if c.isdigit()])
    
    #CALC
    for r in range(0,len(mmap)):
        for c in range(0,len(mmap[0])):
            if r == 0 or c == 0 or r==len(mmap)-1 or c==len(mmap[0])-1:
                visible+=1
            else:
                for p in range (4):
                    if (mmap[r][c] > maxHeight(r, c, p)):
                        visible+=1
                        break
    
    print(visible)


        
        
            
