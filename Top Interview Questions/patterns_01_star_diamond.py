# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.
# Example:
# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****
# *****
#  ***
#   *

def nStarDiamond(n: int) -> None:
    # Write your code here.
    space = n*2 - 1
    for i in range(1,n+1):
        total_spaces = (n*2-1) - (i*2-1)
        star_range = i*2 -1
        f_string = ' '*int((total_spaces/2)) + '*' * star_range + ' '*int((total_spaces/2))
        print(f_string)
    for i in range(n,0,-1):
        total_spaces = (n*2-1) - (i*2-1)
        star_range = i*2 -1
        f_string = ' '*int((total_spaces/2)) + '*' * star_range + ' '*int((total_spaces/2))
        print(f_string)

# nStarDiamond(3)

# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.
# Example:
# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****
# *****
#  ***
#   *

def nStarDiamond_2(n: int) -> None:
    # Write your code here.
    space = n*2 - 1
    for i in range(1,n+1):
        total_spaces = (n*2-1) - (i*2-1)
        star_range = i
        f_string = '*' * star_range + ' '*int((total_spaces/2))
        print(f_string)
    for i in range(n-1,0,-1):
        total_spaces = (n*2-1) - (i*2-1)
        star_range = i
        f_string =  '*' * star_range + ' '*int((total_spaces/2))
        print(f_string)

nStarDiamond_2(3)