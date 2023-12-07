#6: Five of a kind, #5: Four of a kind, #4: Full house, #3: Three of a kind #2: Two pair, #1: One pair, #0: High card
import sys
from collections import Counter

def score(hand: str):
    j = hand.count('J')
    if j == 5 or j == 4: return 6
    v = sorted(Counter(hand.replace('J', "")).values(), reverse=True)
    if v[0] + j > 3: return v[0] + j + 1
    if v[0:2] == [2, 2]: return 4 if j == 1 else 2
    if v[0:2] == [2, 1]: return 3 if j == 1 else 1
    if v[0] + j == 3: return 4 if v[1] == 2 else 3
    return j

print(sum([hand[1] * (index+1) for (index, hand) in enumerate(sorted([(line.split()[0], int(line.split()[1]), score(line.split()[0])) for line in open(sys.argv[1]).readlines()],key=lambda word: (word[2], ['AKQT98765432J'[::-1].index(c) for c in word[0]])))]))


