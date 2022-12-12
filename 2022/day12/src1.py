from pprint import pprint
import sys




heightsMap=[]
minPath=99999999

def backtracking(r, c, list):
    global minPath
    print(len(list))
    if (heightsMap[r][c]=='E' and heightsMap[list[-2][0]][list[-2][1]] == 'z'):
        if len(list)<minPath:
            minPath=len(list)-1
            for i in list:
                print(heightsMap[i[0]][i[1]], end=" ")
            print(minPath)
        return

    if (len(list)>minPath):
        return


    #up
    if r>0 and (ord(heightsMap[r-1][c])<ord(heightsMap[r][c])+2 or heightsMap[r][c] == 'S') and ([r-1,c] not in list):
        backtracking(r-1,c,list+[[r-1,c]])
    #down
    if r<len(heightsMap)-1 and (ord(heightsMap[r+1][c])<ord(heightsMap[r][c])+2 or heightsMap[r][c] == 'S') and ([r+1,c] not in list):
        backtracking(r+1,c,list+[[r+1,c]])
    #left
    if c>0 and (ord(heightsMap[r][c-1])<ord(heightsMap[r][c])+2 or heightsMap[r][c] == 'S') and ([r,c-1] not in list):
        backtracking(r,c-1,list+[[r,c-1]])
    #right
    if c<len(heightsMap[0])-1 and (ord(heightsMap[r][c+1])<ord(heightsMap[r][c])+2 or heightsMap[r][c] == 'S') and ([r,c+1] not in list):
        backtracking(r,c+1,list+[[r,c+1]])


with open(sys.argv[1], "r") as file:
    #READING
    for i, line in enumerate(file):
        heightsMap.append([c for c in line if c.isalpha()])
        
    #CALC
    for r in range(0,len(heightsMap)):
        for c in range(0,len(heightsMap[0])):
            if heightsMap[r][c]=='S':
                backtracking(r,c,[[r,c]])
            
    
print(minPath)

        
        
            
