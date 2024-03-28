# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        map_count = {}
        for el in nums:
            if el not in map_count:
                map_count[el] = 1
            else:
                map_count[el]+=1
            if map_count[el] > len(nums)//2:
                return el



obj = Solution()
el = obj.majorityElement([2,2,1,1,1,2,2])
print(f"El returned {el}")







        
