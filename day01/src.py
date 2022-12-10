import sys

current = {
    "elf": 1,
    "weight": 0
 } #elf number, weight
max = {
    "elf": 1,
    "weight": 0
 } 

with open(sys.argv[1], "r") as file:
    for line in file:
        if line == '\n':
            if current["weight"]>max["weight"]:
                max["weight"] = current["weight"]
                max["elf"] = current["elf"]

            print (max, current)

            current["elf"] += 1
            current["weight"] = 0

        else:
            current["weight"] += int(line.strip())

       
print("MAX = " + str(max["weight"])) 


