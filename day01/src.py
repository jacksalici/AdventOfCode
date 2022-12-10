import sys

weights = [0]

with open(sys.argv[1], "r") as file:
    for line in file:
        if line == '\n':
            weights.append(0)
        else:
            weights[-1] += int(line.strip())

weights.sort(reverse=True)
print(weights[0]+weights[1]+weights[2])

