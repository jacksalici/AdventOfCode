import sys

mmap=[]
maxScenicScore=0

def scenicScore(r, c):
    score = [1,1,1,1]

    col = []
    for i in range(0,len(mmap)):
        for j in range(0,len(mmap[0])):
            if j == c:
                col.append(mmap[i][j])

    
    #up
    for i in col[r-1::-1]:
        if i<mmap[r][c]:
            score[0]+=1
        else:
            break
    
    #down
    for i in col[r+1:]:
        if i<mmap[r][c]:
            score[1]+=1
        else:
            break


    
    #left
    score = 1
    for i in mmap[r][c-1::-1]:
        if i<mmap[r][c]:
            score[2]+=1
        else:
            break


    #right
    for i in mmap[r][c+1:]:
        if i<mmap[r][c]:
            score[3]+=1
        else:
            break

    print(score)
    return score[0]*score[1]*score[2]*score[3]


with open(sys.argv[1], "r") as file:
    #READING
    for i, line in enumerate(file):
        mmap.append([int(c) for c in line if c.isdigit()])
    
    #CALC
    for r in range(1,len(mmap)-1):
        for c in range(1,len(mmap[0])-1):
            currentScenicScore = scenicScore(r, c)
            if (maxScenicScore < currentScenicScore):
                maxScenicScore = currentScenicScore
    
print(maxScenicScore)
