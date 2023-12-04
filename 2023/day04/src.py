import sys
import re

N_WINNER_NUMBERS = 10

scratchcards_total_points = 0

scratchcards_number = {}
scratchcards_number_total = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        matches = re.findall(r'(\d+)', line)
        card_id = int(matches[0])
        card_winners = matches[1:N_WINNER_NUMBERS+1]
        card_numbers = matches[N_WINNER_NUMBERS+1:]
        
        if card_id not in scratchcards_number:
                scratchcards_number[card_id] = 1
        else:
                scratchcards_number[card_id] += 1
                 
        card_com = list(set(card_numbers).intersection(card_winners))

        scratchcards_total_points += 2**(len(card_com)-1) if len(card_com) > 0 else 0
        
        for id in range(card_id+1,card_id+len(card_com)+1):
            if id not in scratchcards_number:
                scratchcards_number[id] = scratchcards_number[card_id]
            else:
                scratchcards_number[id] += scratchcards_number[card_id]
            
        
for n in scratchcards_number.keys():
    scratchcards_number_total += scratchcards_number[n]

print(scratchcards_number_total)