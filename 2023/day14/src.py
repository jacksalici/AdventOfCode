
matrix = []

def text_to_string(filename):
    global matrix
    with open(filename) as f:
        for line in f.readlines():
            matrix.append([c for c in line[:-1]])
            
    
text_to_string('example.txt')

def compute_total_north_north():
    total = 0
    for column_index in range(0, len(matrix[0])):
        max_value = len(matrix)
        for row_index in range(0, len(matrix)):
            cur = matrix[row_index][column_index]
            if cur == 'O':
                total += max_value
                max_value -= 1
            elif cur == '#':
                max_value = len(matrix) - row_index - 1 
        
            if cur != '.':
                print(f"found {cur} at {row_index}, {column_index}. Max value: {max_value}, total: {total}")
    return total


print(compute_total_north_north())

