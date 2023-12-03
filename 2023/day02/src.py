import sys
import re

impossible_id_sum = 0
powers_sum = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        id, game = re.findall(r'Game (\d+): (.+)', line)[0]
        sets = game.split(';')
        
        impossible = False
        
        min_cubes = {'green': 0, 'blue': 0, 'red': 0}
        
        for set in sets:
            cubes = {'green': 0, 'blue': 0, 'red': 0}
            max_cubes = {'red': 12, 'green': 13, 'blue': 14}
            for color in cubes.keys():
                r = re.findall(r'(\d+) '+ re.escape(color), set)
                if len(r)>0:
                    cubes[color] = r[0]
            
                if int(cubes[color])>int(max_cubes[color]):
                    impossible=True
                    
                if int(cubes[color])>int(min_cubes[color]):
                    min_cubes[color] = int(cubes[color])
                
        if(not impossible):
            impossible_id_sum+=int(id)
            
        powers_sum+= min_cubes['blue']*min_cubes['green']*min_cubes['red']

print(f'impossible id sum: {impossible_id_sum}')
print(f'powers sum: {powers_sum}')
                    
            
            
                
                
        