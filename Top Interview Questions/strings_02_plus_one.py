# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


class Solution:
    def __init__(self,digits:list[int]):
        self.digits = digits

    def plusOne(self):
        if self.digits.count(9) == len(self.digits):
            print("test")
            list_ = [1]
            list_.extend([0 for x in self.digits])
            print(list_)
            return list_
        
        if len(self.digits) == 1:
            return [digits[0]+1]
        
        for i in range(len(self.digits)-1,-1,-1):
            # print(i)
            # print(self.digits[i])
            if self.digits[i] == 9:
                self.digits[i] = 0
            else:
                self.digits[i] = self.digits[i] + 1
                return self.digits
            # print(f"digits {self.digits}")

if __name__ == '__main__':
    obj = Solution([8,9,9,9])
    digits = obj.plusOne()
    print(f"digits {digits}")
