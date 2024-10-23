import sys
from functools import cache

REP = 5
springs_representations = list(
	zip(
		((REP*(l.split(" ")[0] + '?'))[:-1] for l in open(sys.argv[1]).readlines()),
		[(int(r) for r in (REP * l.split(" ")[1].strip()).split(",")) for l in open(sys.argv[1]).readlines()]
		
	)
)
for a, b in springs_representations:
	print(a, b)


possibilites = []
@cache
def rec(str: str, index: int, groups):
	if index==len(str):
		#print(groupBy(str), groups)
		if groupBy(str) == groups:
			possibilites.append(str)
		return
	if str[index]=='?':
		rec(str.replace('?', '.', 1), index+1, groups)
		rec(str.replace('?', '#', 1), index+1, groups)
	else:
		rec(str, index+1, groups)
	

def groupBy(str: str) -> list: 
	from itertools import groupby
	return [len("".join(g)) for k, g in groupby(str) if k != '.']

for str, groups in springs_representations:
	rec(str, 0, groups)

print(len(possibilites))
