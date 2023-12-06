import sys
import re
import math

records=1
with open(sys.argv[1]) as f:
    lines = f.readlines()
    times = [int(x) for x in re.findall(r"(\d+)", lines[0])]
    distances = [int(x) for x in re.findall(r"(\d+)", lines[1])]
    
    ##BRUTE FORCE
    for (time, distance) in zip (times, distances):
        record=0
        for i in range(0, time+1):
            if (time-i)*i>distance:
                record+=1
        records*=record
    
    print(records)

    ##MATH WAY
    records=1
    for (time, distance) in zip (times, distances):
        for i in range(0, time + 1):
            if (time-i)*i>distance:
                records*=time-2*i+1
                break
        
    print(records)
    
