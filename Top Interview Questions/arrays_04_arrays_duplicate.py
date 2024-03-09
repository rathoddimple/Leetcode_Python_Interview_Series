# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDuplicate(nums):
    nums.sort()
    if len(nums) == 1:
        return False
    for i in range(0,len(nums)-1):
        # print(f"current {nums[i]}")
        # print(f"next {nums[i+1]}")
        if nums[i] == nums[i+1]:
            return True
    if nums[-1] == nums[len(nums)-2]:
        return True
    else:
        return False
            
        

arr = [2,14,18,22,22]        
st = containsDuplicate(arr)          
print(f"{st}")
arr = [1,2,3,4]
st = containsDuplicate(arr)          
print(f"{st}")
arr = [0]
st = containsDuplicate(arr)          
print(f"{st}")
