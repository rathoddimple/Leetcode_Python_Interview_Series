
# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.

 

# Example 1:

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:

# Input: s = "", t = "y"
# Output: "y"
 

# Constraints:

# 0 <= s.length <= 1000
# t.length == s.length + 1
# s and t consist of lowercase English letters.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        else:
            s_list = [char for char in s]
            t_list = [char for char in t]
            s_list.sort()
            t_list.sort()
            for i in range(len(s_list)):
                if s_list[i] != t_list[i]:
                    return t_list[i]
            return t_list[-1]
            

obj = Solution()
char = obj.findTheDifference("abcd","acebd")
print(f"Difference char = {char}")