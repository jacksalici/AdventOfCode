import sys
priorities = 0

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)

with open(sys.argv[1], "r") as file:
    for c1, c2, c3 in grouped(file, 3):    
        common = set(c1.strip()) & set(c2) & set(c3)
        for elem in common: 
            priorities += (ord(elem)-96) if elem.islower() else (ord(elem)-38)
        
print(priorities)