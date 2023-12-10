import sys, re
pipes = open(sys.argv[1]).readlines()
pipes_lenght = 1
s = 'L' # MANUAL INPUT
def direction_feasibility(src_row, src_col):
    return {
        'N': src_row>0,
        'S': src_row<len(pipes)-1,
        'W': src_col>0,
        'E': src_col<len(pipes[src_row])-1
    }   

src_row, src_col = (0, 0) #row, col
while pipes[src_row].find('S')<0: 
    src_row += 1
src_col = pipes[src_row].find('S')
    
      
loop_border = set()

there_is_dir = direction_feasibility(src_row, src_col) 
     
if there_is_dir['S'] and (pipes[src_row+1][src_col] == 'L' or pipes[src_row+1][src_col] =='|' or pipes[src_row+1][src_col] == 'J'):
    find_next = (src_row+1, src_col, 'S')
elif there_is_dir['N'] and (pipes[src_row-1][src_col] == '7' or pipes[src_row-1][src_col] =='|' or pipes[src_row-1][src_col] == 'F'):
    find_next = (src_row-1, src_col, 'N')
elif there_is_dir['W'] and (pipes[src_row][src_col-1] == 'L' or pipes[src_row][src_col-1] =='-' or pipes[src_row][src_col-1] == 'F'):
    find_next = (src_row, src_col-1, 'W')
elif there_is_dir['E'] and (pipes[src_row][src_col+1] == 'J' or pipes[src_row][src_col+1] =='-' or pipes[src_row][src_col+1] == '7'):
    find_next = (src_row, src_col+1, 'E')

pipe = pipes[src_row][src_col]


while(1):
    loop_border.add((src_row, src_col))
    src_row, src_col, direction = find_next
    pipe = pipes[src_row][src_col]
    there_is_dir = direction_feasibility(src_row, src_col)      
    old_find_next = find_next

    if pipe == 'S':
        break    

    pipes_lenght+=1    
    match pipe:
        case '|':
            if direction=='S' and there_is_dir['S']:
                find_next = (src_row+1, src_col, 'S')
            if direction=='N' and there_is_dir['N']:
                find_next = (src_row-1, src_col, 'N')
        case '-':
            if direction=='E' and there_is_dir['E']:
                find_next = (src_row, src_col+1, 'E')
            if direction=='W' and there_is_dir['W']:
                find_next = (src_row, src_col-1, 'W')
        case 'L':
            if direction=='S' and there_is_dir['E']:
                find_next = (src_row, src_col+1, 'E')
            if direction=='W' and there_is_dir['N']:
                find_next = (src_row-1, src_col, 'N')
        case 'J':
            if direction=='S' and there_is_dir['W']:
                find_next = (src_row, src_col-1, 'W')
            if direction=='E' and there_is_dir['N']:
                find_next = (src_row-1, src_col, 'N')
        case '7':
            if direction=='N' and there_is_dir['W']:
                find_next = (src_row, src_col-1, 'W')
            if direction=='E' and there_is_dir['S']:
                find_next = (src_row+1, src_col, 'S')
        case 'F':
            if direction=='N' and there_is_dir['E']:
                find_next = (src_row, src_col+1, 'E')
            if direction=='W' and there_is_dir['S']:
                find_next = (src_row+1, src_col, 'S')

    assert old_find_next!=find_next
print("MAX PIPE DISTANCE", pipes_lenght/2)
print("LOOP LENGHT", len(loop_border))


#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.

inside_block=0
for row_index, row_pipes in enumerate(pipes):
    outside=True
    
    qJ = False
    q7 = False
    

    
    for col_index, pipe in enumerate(row_pipes):
        if(row_index, col_index) in loop_border:
            match pipe:
                case '|':
                    outside = not outside
                case 'F':
                    qJ = True
                case 'L':
                    q7 = True
                case 'J':
                    if qJ:
                        outside = not outside
                        qJ = False
                    q7 = False
                case '7':
                    if q7:
                        outside = not outside
                        q7 = False
                    qJ = False 
       
        else:
            if not outside:
                inside_block+=1
                #print (row_index, col_index)
                
print("INSIDE BLOCK", inside_block)