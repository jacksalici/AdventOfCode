import sys
import re
from typing import List

class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.maps = []

    def addMap(self, dest, src, len) -> None:
        self.maps.append({"dest": dest, "src": src, "len": len, "offset":dest-src})

    def convert(self, input):
        output = []
        
        while input:
            (start, end) = input.pop()
            found = False
            
            for map in self.maps:
                actual_start = max(start, map["src"])
                actual_end = min(end, map["src"]+map["len"])
                
                if actual_start<actual_end:
                    output.append((actual_start+map["offset"], actual_end+map["offset"]))
                    
                    if start<actual_start:
                        input.append((start,actual_start))
                    if end>actual_end:
                        input.append((actual_end,end))
                    found = True
                    break


            if not found:
                output.append((start,end))

        return output

categories:List[Category] = [] 

with open(sys.argv[1]) as f:
    lines = f.readlines()
    intitial_seeds = [int(x) for x in re.findall(r"(\d+)", lines[0])]

    for line in lines[1:]:
        
        category = re.match(r'([\w-]+) map:', line)
        
        if category:
            categories.append(Category(category.groups()[0]))
            continue
        
        t = re.findall(r'(\d+)', line)
        
        if(len(t)==3):
            categories[-1].addMap(int(t[0]), int(t[1]), int(t[2]))
        
print("Almanac category: ", len(categories))
from operator import add

locations = list(zip(intitial_seeds[::2], list(map(add, intitial_seeds[::2], intitial_seeds[1::2]) ) ))
print("Initial Seeds locations: ", locations)

    
for category in categories:
    locations = category.convert(locations)

print("Final location:", min(locations)[0]) 
