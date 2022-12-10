import sys

totalscore = 0
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Rock defeats Scissors, 
# Scissors defeats Paper, 
# and Paper defeats Rock.

def outcome(myMove, elfsMove):
    if chr(ord(myMove)-23) == elfsMove:
        return 3
    elif (myMove == 'X' and elfsMove == 'C') \
        or (myMove == 'Z' and elfsMove == 'B') \
            or (myMove == 'Y' and elfsMove == 'A'):
        return 6
    else:
        return 0

def shape(myMove):
    if myMove == 'X':
        return 1
    elif myMove == 'Y':
        return 2
    else:
        return 3

with open(sys.argv[1], "r") as file:
    for line in file:
        plays = line.strip().split(" ")
        totalscore+=shape(plays[1]) + outcome(plays[1],plays[0])


print (totalscore)

