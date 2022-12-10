import sys

priorities = 0
with open(sys.argv[1], "r") as file:
    for line in file:
        c1,c2=line[:len(line)//2], line[len(line)//2:]
        common = set(c1) & set(c2)
        for elem in common: 
            priorities += (ord(elem)-96) if elem.islower() else (ord(elem)-38)
        
print(priorities)