# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# test = [1,0,3,12,0]
# index = 1
# test = test[:index] + test[index+1:] + [0]
# print(test)


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def array_new(nums,index):
            nums = nums[:index] + nums[index+1:] + [0]
            return nums


        def index_checker(nums,index):
            if nums[index] == 0:
                nums = array_new(nums,index)
                if index!=0:
                    index = index - 1
                else:
                    index = index 
                return nums, index
            return nums, index+1

        def other_method(nums):      
            og_index = 0
            index = 0
            while og_index != len(nums) -1:
                nums,index = index_checker(nums,index)
                og_index=og_index+1
            print(f"Final {nums}")
        
        # Move Zeros
        og_index = 0
        index = 0
        while og_index != len(nums) -1:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
            else:
                index = index + 1
            og_index=og_index+1
        print(f"Moved Zeros {nums}")


obj = Solution()
obj.moveZeroes([0,1,0,3,12])


                
       
