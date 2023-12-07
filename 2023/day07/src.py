import sys
alphabet = "23456789TJQKA"

hands = []

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        elem = line.split(" ")
        hand = elem[0]
        bid = int(elem[1])
        type = 0
        
        couple = 0
        triple = 0
        for s in alphabet: 
            c = hand.count(s)
            if c == 5:
                type=6
                break
            if c == 4:
                type=5
                break
            if c == 3:
                triple+=1
            if c == 2:
                couple+=1
        if couple == 1 and triple == 1:
            type = 4
        elif couple == 0 and triple == 1:
            type = 3
        elif couple == 2 and triple == 0:
            type = 2
        elif couple == 1:
            type = 1
                
        hands.append((hand, bid, type))

hands = sorted(hands, key=lambda word: (word[2], [alphabet.index(c) for c in word[0]]))

winnings = 0
for index, hand in enumerate(hands ):
    winnings += hand[1] * (index+1)
print("Total winnings: ", winnings)