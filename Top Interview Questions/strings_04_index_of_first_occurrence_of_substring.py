# 28. Find the Index of the First Occurrence in a String
# Easy

# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

#Implementing Polynomial Rolling Hash function to compare hash of sliding window substring in string and target substring
"""
Rolling Hash Function - For substring matching
A rolling hash is a hash function that is used to efficiently compute a hash value for a sliding window of data. 
It is commonly used in computer science and computational biology, where it can be used to detect approximate string matches, 
find repeated substrings, and perform other operations on sequences of data.
let’s say we have a string “hello world” and we want to search for the substring “world” within it. We can use the Rabin-Karp hash function to compute the hash value of each possible substring of length 5 (the length of the substring “world”) and compare it to the hash value of the target substring “world”.
To compute the hash value of a substring, the Rabin-Karp algorithm uses a rolling hash function that maintains a running hash value of the current substring and updates the hash value as the sliding window moves across the input string.
For instance, the Rabin-Karp rolling hash function might use the following formula to compute the hash value of a substring:
hash(substring) = (c1 * a^(k-1) + c2 * a^(k-2) + … + ck * a^0) mod m where c1, c2, …, ck are the ASCII values of the characters in the substring, a is a prime number (e.g., 31), k is the length of the substring, and m is a large prime number (e.g., 10^9 + 7).
""" 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def generate_hash_of_substring(start_index,end_index,string):
            #Hash = s[0] + s[1]*p + s[2]*p^2 +...s[n-1]*p^(n-1) %m
            p = 31
            m = 10**9 + 7
            p_pow = 1
            calculated_hash = 0
            for i in range(start_index,end_index,1):
                calculated_hash = (calculated_hash + (1 + ord(string[i]) - ord('a'))*p_pow)%m
                p_pow = (p_pow*p)%m
            print(f"{calculated_hash}")
            return calculated_hash
        

        #Edge Case 
        if len(haystack) == 1:
            if haystack == needle:
                return 0

        needle_hash = generate_hash_of_substring(0,len(needle),needle)
        for i in range(0,len(haystack)-len(needle),1):
            substrng_hash = generate_hash_of_substring(i,i+len(needle),haystack)
            print(f"hash for substring start index {i} {substrng_hash}")
            if substrng_hash == needle_hash:
                return i
            
        #Edge Case
        if haystack[len(haystack)-len(needle):] == needle:
            return len(haystack)-len(needle)
        return -1
        

obj = Solution()
index = obj.strStr('abc','c')
print(f"Index {index}")
        

        
               