import sys
import re
import math

with open(sys.argv[1]) as f:
    lines = f.readlines()
    time = int("".join(re.findall(r"(\d+)", lines[0])))
    distance = int("".join(re.findall(r"(\d+)", lines[1])))
    
    
    records=0
    for i in range(0, time + 1):
        if (time-i)*i>distance:
            records+=time-2*i+1
            break
        
    print(records)
    
   
