import sys
from pprint import pprint
import re

matrixOfCrates1 = [[] for i in range (int(sys.argv[3]))]
matrixOfCrates2 = [[] for i in range (int(sys.argv[3]))]

#move 1 from 4 to 1
def exeCommand1(c):
    for i in range(0, int(c[0])):
        matrixOfCrates1[int(c[2])-1] += matrixOfCrates1[int(c[1])-1].pop()

def exeCommand2(c):
    matrixOfCrates2[int(c[2])-1] += matrixOfCrates2[int(c[1])-1][-int(c[0]):]
    del matrixOfCrates2[int(c[1])-1][-int(c[0]):]

def createMatrix(line):
    for i, char in enumerate(line):
                if (i-1)%4==0 and char != ' ':
                    matrixOfCrates1[int((i-1)/4)].insert(0,char)
                    matrixOfCrates2[int((i-1)/4)].insert(0,char)


with open(sys.argv[1], "r") as file:
    for index, line in enumerate(file):
        if index<int(sys.argv[2]):
            createMatrix(line)
        elif index>int(sys.argv[2])+1: #split the input file by hand
            exeCommand1(re.findall("(\d+)", line))
            exeCommand2(re.findall("(\d+)", line))
            
        

pprint(matrixOfCrates2)
       
word = ""
for i in matrixOfCrates2:
    word+=i[-1]

print(word)