import sys
from collections import Counter

a = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']

#249781879
hands = []

def score(hand):
    couple = 0
    triple = 0
    quaple = 0
    
    for s in a: 
        c = hand.count(s)
        if c == 5:
            return 6 
        if c == 4:
            quaple += 1
        if c == 3:
            triple+=1
        if c == 2:
            couple+=1
            
    if quaple:
        return 5        

    if couple == 1 and triple == 1:
        return 4
        
    elif couple == 0 and triple == 1:
        return 3
    elif couple == 2 and triple == 0:
        return 2
    elif couple == 1:
        return 1
    else:
        return 0


def best_score(hand: str):
    possibilities = []
    
    for J in a[:-1]:
        possibilities.append(score(hand.replace("J", J)))
    
    return(max(possibilities))


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        elem = line.split(" ")
        hand = elem[0]
        bid = int(elem[1])
        type = best_score(hand)
                
        hands.append((hand, bid, type))


hands = sorted(hands, key=lambda word: (word[2], [a[::-1].index(c) for c in word[0]]))
winnings = 0
for (index, hand) in enumerate(hands):
    winnings += hand[1] * (index+1)
print("Total winnings: ", winnings)

