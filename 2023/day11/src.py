import sys, math
from typing import List

line_lenght = 0


class Galaxy:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"gal({self.x},{self.y})"

galaxies:List[Galaxy] = []


## READ AND EXPANSION
void_rows = []
void_cols = []
for row, line in enumerate(open(sys.argv[1]).readlines()):
	void_row = True
	for col, char in enumerate(line):
		if char == '#':
			galaxies.append(Galaxy(row, col))
			void_row == False
	
	if void_row:
		void_rows.append(row)
	line_lenght = len(line)

j = 0
while j<line_lenght: 
	if all(g.y!=j for g in galaxies):
		void_cols.append(j)
	j+=1
  
	 
# [[0, 4], [1, 9], [2, 0], [5, 8], [6, 1], [7, 12], [10, 9], [11, 0], [11, 5]]


def compareX(a: Galaxy, b: Galaxy):
	return (a.x - b.x)

def compareY(a:Galaxy, b:Galaxy):
	return a.y - b.y

EXPANSION_FACTOR=1

def dist(p1: Galaxy, p2: Galaxy):
	return abs(p1.x - p2.x) + sum(p1.x<i<p2.x for i in void_rows)*EXPANSION_FACTOR + abs(p1.y - p2.y) + sum(p1.y<j<p2.y for j in void_cols)*EXPANSION_FACTOR

 	 

total_pairs = 0

total_sum = 0
print(galaxies)
for index, i in enumerate(galaxies):
	for j in galaxies[index+1:]:
		total_pairs+=1
		total_sum+=dist(i, j)
			
			
print(total_pairs, total_sum)