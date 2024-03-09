# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(i: int, j: int):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    n = len(nums)
    k %= n
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

def switch(index,array):
    print(f"array before change {array}")
    switch_el = array[len(array)-1]
    # print(f"swith_el {switch_el}")
    for i in range(len(array)-1,index,-1):
        # print(f"switch {array[i]}")
        # print(f"{array[i-1]}")
        array[i] = array[i-1]
    array[index] = switch_el
    print(f"changed {array}")

def switch_2(k,nums):
    while k!=0:
        nums_copy = nums.copy()
        nums[0] = nums_copy[-1]
        for i in range(0,len(nums_copy)-1):
            nums[i+1] = nums_copy[i]
        k-=1

def switch_3(nums,k):
     nums = (nums[len(nums) - k:len(nums)] 
                 + nums[0:len(nums) - k])
      
                
def rotate_2(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = k
        while k !=0:
            switch(0,nums)
            k-=1
        # print(f"nums 2 {nums}")
            
nums = [1,2,3,4,5,6,7]
# print(f"{nums[-1]}")
new_nums = rotate(nums,3)
print(f"new nums {new_nums}")
# print(len(nums))
# index = len(nums)-1
# print(nums[len(nums)-1])
