import sys, numpy as np

patterns = open(sys.argv[1]).read().split("\n\n")

sum = 0
for p in patterns:
    
    r = np.array([[e == '#' for e in line] for line in p.split("\n")] )
    print (r)

    for index in range(1, len(rows)):
        m = min(index, len(rows)-index)
            #f = all[rows[index] == rows[index+1 + n] for n in range(m)]
            #print(rows[index-m:index],"        ",list(reversed(rows[index:index+m])))
        if rows[index-m:index]==list(reversed(rows[index:index+m:-1])):
            sum += index * (100 if rows == r else 1)
            print(rows, index+1)
            break
        
    
    
    
    
            
print(sum)