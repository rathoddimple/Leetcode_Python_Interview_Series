# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #quick sort
        def partitionIndex(arr,low,high,):
            if low>=high:
                return
            pivot = arr[low]
            i = low
            j = high 
            while i<j:
                while arr[i]<=pivot and i<=high-1:
                    i+=1
                while arr[j] > pivot and j>=low+1:
                    j-=1
                #Swap required elements
                if i<j:
                    arr[i],arr[j] = arr[j], arr[i]
            #Swap pivot and j index element
            arr[low], arr[j] = arr[j], arr[low]
            return j
        
        def quicksort(arr,startindex,endindex):
            l=startindex
            h=endindex
            if l<h:
                p_Index = partitionIndex(arr,l,h)
                quicksort(arr,l,p_Index-1)
                quicksort(arr,p_Index+1,h)
            return arr

        if m+n == 1:
            if m == 0:
                nums1[0] = nums2[0]
            elif n == 0:
                nums1[0] = nums1[0]
        else:           
            pointer_2 = 0
            for i in range(m,len(nums1)):
                nums1[i] = nums2[pointer_2]
                pointer_2+=1
            num1s = quicksort(nums1,0,len(nums1)-1)
        print(f"Merged = {nums1}")

obj = Solution()
# obj.merge([1,2,3,0,0,0],3,[2,5,6],3)
# obj.merge([1],1,[],0)
# obj.merge([0],0,[1],1)
# obj.merge([1,2,3,4,5],5,[],0)
obj.merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)
        