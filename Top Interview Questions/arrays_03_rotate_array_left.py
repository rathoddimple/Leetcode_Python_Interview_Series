
# Ex:
# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2



def rotate_left(d,arr):
    while d > 0:
        print(f"d val {d}")
        arr.append(arr[0])
        del arr[0]
        d-=1
        print(f"current arr {arr}")
    return arr 
    
array_test = [1,2,3,4,5,6,7]
arr_new = rotate_left(2,array_test)
print(f"New rotated array = {arr_new}")


        
