board = [
    [0,5,0,0,0,0,1,9,0],
    [0,0,0,0,0,0,0,4,2],
    [9,1,0,0,2,7,5,6,8],
    [3,4,5,0,0,1,9,0,6],
    [7,0,0,3,4,0,0,0,0],
    [8,9,0,2,0,6,0,0,3],
    [0,0,8,7,0,0,2,1,0],
    [1,6,0,0,0,8,0,0,4],
    [0,0,0,1,0,0,6,8,5]
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")
        
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None          
                
def ok(bo, num, pos):
    # Check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check Column            
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check 3x3 Square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
        
    return True

def solve(bo):
    empty = find_empty(bo)
    if not empty:
        return True
    else:
        row, col = empty
    
    for i in range (1, 10):
        if ok(bo,i,(row,col)):
            bo[row][col] = i
            
            if (solve(bo)):
                return True
            bo[row][col] = 0
    return False