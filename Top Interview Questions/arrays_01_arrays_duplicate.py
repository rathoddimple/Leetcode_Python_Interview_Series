# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

array_1 = [0,0,1,1,1,2,2,3,3,4]
output = [0,1,2,3,4,0,1,1,2,3]

def switch(array,index_1,index_2):
    temp = array[index_1]
    array[index_1] = array[index_2]
    array[index_2] = temp


curr_index = 0
unique_el = []
for i in range(0,len(array_1)):
    curr_el = array_1[i]
    if curr_el not in unique_el:
        unique_el.append(array_1[i])
        print(f"unique element detected {array_1[i]}")
        switch(array_1,curr_index,i)
        curr_index +=1
        print(f"new array {array_1}")

class Solution:
    def switch(self,array,index_1,index_2):
        temp = array[index_1]
        array[index_1] = array[index_2]
        array[index_2] = temp
        
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_index = 0
        unique_el = []
        for i in range(0,len(nums)):
            curr_el = nums[i]
            if curr_el not in unique_el:
                unique_el.append(nums[i])
                # print(f"unique element detected {nums[i]}")
                self.switch(nums,curr_index,i)
                curr_index +=1
                # print(f"new array {nums}")
        return curr_index


