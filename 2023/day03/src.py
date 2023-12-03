import sys
import re

gear_ratios_sum = 0
part_number_sum = 0
gears=[]

def isSymbol(char: str):
    return ((not char.isdigit()) and (char!='.'))

def checkAndAddGear(char, char_index, line_index, number):
    if (char == '*'):
        new_gear = {"position": (char_index, line_index), "part_numbers": [number]}
        present = False
        for gear in gears:
            if gear["position"] == new_gear['position']:
                gear["part_numbers"].append(number)
                present = True
        
        if not present:
            gears.append(new_gear)
        
    

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line_index, line in enumerate(lines):
        matches = re.finditer(r'(\d+)', line)
        for m in matches:
            is_part_number = False
            
            start = m.start() - 1 if m.start() > 0 else m.start()
            check_left = True if m.start() > 0 else False
            
            end = m.end() if m.end() < len(line) - 1 else m.end()-1
            check_right = True if m.end() < len(line) - 1 else False
            
            for chars_index in range(start, end+1):
                #check above
                if (line_index > 0):          
                    if isSymbol(lines[line_index-1][chars_index]):
                       is_part_number = True
                       checkAndAddGear(lines[line_index-1][chars_index], line_index-1, chars_index, m.group())
                       
                    
                
                #check below
                if (line_index < len(lines)-1):          
                    if isSymbol(lines[line_index+1][chars_index]):
                        is_part_number = True
                        checkAndAddGear(lines[line_index+1][chars_index], line_index+1, chars_index, m.group())
                       
                   
            #check left
            if check_left:
                if isSymbol(lines[line_index][start]):
                    is_part_number = True
                    checkAndAddGear(lines[line_index][start], line_index, start, m.group())
            
            #check right
            if check_right:
                if isSymbol(lines[line_index][end]):
                    is_part_number = True
                    checkAndAddGear(lines[line_index][end], line_index, end, m.group())
            
            if is_part_number:
                part_number_sum+=int(m.group())
            

print("Total part number sum: ", part_number_sum)

for gear in list(gears):
    if (len(gear["part_numbers"])!=2):
        gears.remove(gear)

for gear in gears:
    gear_ratios_sum += int(gear["part_numbers"][0]) * int(gear["part_numbers"][1])

print("Total gear ratios: ", gear_ratios_sum)