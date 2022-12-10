import sys

totalscore = 0
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Rock defeats Scissors, 
# Scissors defeats Paper, 
# and Paper defeats Rock.

# X means you need to lose,
# Y means you need to end the round in a draw
# and Z means you need to win

def calculateMove(outcome, elfsMove):
    if (outcome == 'Y'):
        return chr(ord(elfsMove)+23)
    elif (outcome == 'X'):
        if (elfsMove == 'A'):
            return 'Z'
        elif (elfsMove == 'B'):
            return 'X'
        else:
            return 'Y'
    else:
        if (elfsMove == 'A'):
            return 'Y'
        elif (elfsMove == 'B'):
            return 'Z'
        else:
            return 'X' 

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
        inputs = line.strip().split(" ")
        myMove = calculateMove(inputs[1],inputs[0])
        totalscore+=shape(myMove) + outcome(myMove,inputs[0])


print (totalscore)

