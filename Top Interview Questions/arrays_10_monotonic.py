class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        def compare_arr(arr,copy):
            for i in range(len(nums)-1):
                if nums[i] != nums_copy[i]:
                    return False
            return True
                    
        nums_copy = nums.copy()
        nums.sort()
        asc_status = compare_arr(nums,nums_copy)
        nums.sort(reverse=True)
        desc_status = compare_arr(nums,nums_copy)
        if asc_status or desc_status:
            return True
        else:
            return False
        
obj = Solution()
monotonic = obj.isMonotonic([1,3,2])
print(f"Array is monotonic: {monotonic}")