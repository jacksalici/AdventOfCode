import sys, re, numpy
histories = [[int(x) for x in re.findall(r'\S+', line)] for line in open(sys.argv[1]).readlines()]

sum_of_nexts = 0
sum_of_prevs = 0

for h in histories:
    diffs = [h]
    
    while(any(x!=0 for x in diffs[-1])):
        diffs.append(numpy.diff(diffs[-1]))
    
    prev = 0
    for d in diffs[::-1]:
        sum_of_nexts+=d[-1]
        prev = d[0] - prev
    sum_of_prevs+=prev

  
    
    
print(sum_of_nexts, sum_of_prevs)