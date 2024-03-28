# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == len(t):
            if len(s) == 1:
                if s == t:
                    return True
        s_arr = list(s)
        map_s = {}
        for i in range(len(s_arr)):
            if s_arr[i] in map_s:
                map_s[s_arr[i]] +=1
            else:
                map_s[s_arr[i]] = 1
        t_arr = list(t)
        for el,count_el in map_s.items():
            if el in t_arr and count_el == t_arr.count(el):
                continue
            else:
                return False
        return True
    
    def isPalindrome(self, s: str) -> bool:
        s_new = s
        for i in range(len(s)):
            if not(s[i:i+1].isalpha()) and not(s[i:i+1].isnumeric()):
                s_new = s_new.replace(s[i:i+1],"")
            if not(s[i:i+1].islower()):
                s_new = s_new.replace(s[i:i+1],s[i:i+1].lower())
        if len(s_new) == 1:
            return True
        for i in range(int(len(s_new)/2)):
            if s_new[i:i+1] != s_new[len(s_new)-i-1:len(s_new)-i]:
                return False
        return True



# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
    

obj = Solution()
# is_anagram = obj.isAnagram("anagram","nagaram")
# print(f"Anagram: {is_anagram}")
is_palindrome = obj.isPalindrome("0P")
print(f"Palindrome {is_palindrome}")
        
