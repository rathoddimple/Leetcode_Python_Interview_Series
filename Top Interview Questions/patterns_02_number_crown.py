# 1                         1
# 1 2                     2 1
# 1 2 3                 3 2 1
# 1 2 3 4             4 3 2 1
# 1 2 3 4 5         5 4 3 2 1
# 1 2 3 4 5 6     6 5 4 3 2 1
# 1 2 3 4 5 6 7 7 6 5 4 3 2 1  

def numberCrown(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(1,(n*2 - i*2)+1):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

# numberCrown(3)

# Input: ‘N’ = 3

# Output: 
#     A
#   A B A
# A B C B A

def alphaHill(n: int):
    start = 64
    for i in range(1,n+1):
        space = n - i
        for j in range(1,space+1):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(chr(j+start),end=" ")
        for j in range(i-1,0,-1):
            print(chr(j+start),end=" ")
        for j in range(1,space+1):
            print(" ",end=" ")
        print()

alphaHill(3)
        
