# Example 2:

# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-231, 231 - 1], the final result is -42.
# Example 3:

# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 : 
            return 0
        ls = list(s.strip())
        if len(ls) == 0 : 
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : 
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + int(ls[i])
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
    

obj = Solution()
num = obj.myAtoi("words and 987")
print(f"Num {num}")
 