import sys

PART_TWO = 1

calibrations_sum = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        if PART_TWO == 1:
            numb = {"one" : 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

            for spelling, digit in numb.items():
                line = line.replace(spelling, spelling+str(digit)+spelling)
        
        
        first = {"found": False, "value": 0}
        last = {"found": False, "value": 0}
        
        for letter in line:
            if str(letter).isdigit():
                if not first["found"]:
                    first["found"] = True
                    first["value"] = int(letter)
                last["found"] = True
                last["value"] = int(letter)
        
        if first["found"] and last["found"]:        
            calibration = first["value"] * 10 + last["value"]
        else:
            calibration = 0
        
        calibrations_sum+=calibration
        print(calibration)
    
print(calibrations_sum)