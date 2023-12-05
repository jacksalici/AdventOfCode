import sys
import re
from typing import List

class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.maps = []

    def addMap(self, dest, src, len) -> None:
        self.maps.append({"dest": dest, "src": src, "len": len})

    def convert(self, input):
        output = []
            
        while input:
            (start, end) = input.pop()
            found = False
            assert start<end
            
            for map in self.maps:
                
                
                map_start = map["src"]
                map_len = map["len"]
                map_end = map_start + map_len
                map_dest_start = map["dest"]
                
                if end < map_start and start < map_start:
                    continue
                if end <= map_end and start < map_start:
                    input.append((start, map_start))
                    output.append((map_dest_start,map_dest_start+end-(map_start)))
                    found = True
                if end <= map_end and start >= map_start:
                    output.append((map_dest_start+(start-map_start),map_dest_start+(end-map_start)))
                    found = True
                if end > map_end and start >= map_start:
                    input.append((map_end, end))
                    output.append((map_dest_start+(start-map_start),map_dest_start+(map_end-map_start)))
                    found = True
                if end < map_start and start < map_start:
                    continue

            if not found:
                output.append((map_dest_start+(start-map_start),map_dest_start+(end-map_start))) 

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

locations = list(zip(intitial_seeds[::2], list( map(add, intitial_seeds[::2], intitial_seeds[1::2]) ) ))
print("Initial Seeds locations: ", locations)

    
for category in categories:
    locations = category.convert(locations)

print("Final location:", locations) 
