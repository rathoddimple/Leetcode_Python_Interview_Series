class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        if len(s) == 1:
            return 0
        unique_el = []
        for c in range(0,len(s)):
            if s[c] not in unique_el:
                unique_el.append(s[c])
                if s.count(s[c]) == 1:
                    return c
        return -1
        

obj = Solution()
s = obj.firstUniqChar("dddccdbba")
print(s)