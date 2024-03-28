
# Input: ‘N’ = 4

# Output: 

# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

def getNumberPattern(n: int) -> None:
    for row in range(0,2*n-1):
        for col in range(0,2*n-1):
            dist_of_cell_from_top = row
            dist_of_cell_from_left = col
            dist_of_cell_from_right = (2*n-2)-col
            dist_of_cell_from_down = (2*n-2)-row
            print(n-min(dist_of_cell_from_left,dist_of_cell_from_right,dist_of_cell_from_top,dist_of_cell_from_down),end="")
        print()

getNumberPattern(4)