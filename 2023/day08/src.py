import sys, re,math
PART = 2 # 1 / 2

nodes = { re.findall(r'[0-9A-Z]{3}', line)[0]: (re.findall(r'[0-9A-Z]{3}', line)[1], re.findall(r'[0-9A-Z]{3}', line)[2]) for line in open(sys.argv[1]).readlines()[2:] }
map = [0 if letter=='L' else 1 for letter in open(sys.argv[1]).readline()[:-1]]


steps = []
startNodesKey = list(filter(lambda n: (n[2]=='A') if PART == 2 else (n == 'AAA'), nodes))
for node in (startNodesKey):
    i = 0
    while(True):
        if PART == 1 and node == 'ZZZ':
            break
        elif PART == 2 and node[2] == 'Z':
            break
        else: 
            node = nodes[node][map[i%len(map)]]
        i+=1
    steps.append(i)

print(math.lcm(*steps))