import sys
import re
from typing import List

class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.maps = []

    def addMap(self, dest, src, len) -> None:
        self.maps.append({"dest": int(dest), "src": int(src), "len": int(len)})

    def convert(self, input):
        for map in self.maps:
            if map["src"] <= int(input) <= map["src"] + map["len"]:
                return map["dest"] + (int(input) - map["src"])

        return int(input)

categories:List[Category] = [] 

with open(sys.argv[1]) as f:
    lines = f.readlines()
    intitial_seeds = re.findall(r"(\d+)", lines[0])

    for line in lines[1:]:
        
        category = re.match(r'([\w-]+) map:', line)
        
        if category:
            categories.append(Category(category.groups()[0]))
            continue
        
        t = re.findall(r'(\d+)', line)
        
        if(len(t)==3):
            categories[-1].addMap(t[0], t[1], t[2])
        
print("Initial Seeds: ", intitial_seeds)
print("Almanac category: ", len(categories))

locations = []
for seed in intitial_seeds:
    number = seed
    for category in categories:
        number = category.convert(number)
    locations.append(number)

print("Final location:", locations)
print("Minimum: ", min(locations))