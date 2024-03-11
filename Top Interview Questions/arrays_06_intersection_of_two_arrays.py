# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def unique_el(lst):
            unique_list = []
            for x in lst:
                if x not in unique_list:
                    unique_list.append(x)
            return unique_list
        
        def generate_result_list(checking_unique_list,checkee_unique_list, checking_list, checkee_list):
            result_lst = []
            for x in checking_unique_list:
                if x in checkee_unique_list:
                    freq = min(checking_list.count(x),checkee_list.count(x))
                    result_lst += freq * [x]
            return result_lst
        
        nums1.sort()
        nums2.sort()
        unique_list_1 = unique_el(nums1)
        unique_list_2 = unique_el(nums2)
        if len(unique_list_1) > len(unique_list_2):
            result_list = generate_result_list(checking_unique_list=unique_list_1,checkee_unique_list=unique_list_2,checking_list=nums1,checkee_list=nums2)
        else:
            result_list = generate_result_list(checking_unique_list=unique_list_2,checkee_unique_list=unique_list_1,checking_list=nums2,checkee_list=nums1)
        return result_list



obj = Solution()
result_list = obj.intersect([1,2,2,1],[2,2])
print(f"Result_array {result_list}")
        
