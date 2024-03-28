"""
Rolling Hash Function - For substring matching
A rolling hash is a hash function that is used to efficiently compute a hash value for a sliding window of data. 
It is commonly used in computer science and computational biology, where it can be used to detect approximate string matches, 
find repeated substrings, and perform other operations on sequences of data.
let’s say we have a string “hello world” and we want to search for the substring “world” within it. We can use the Rabin-Karp hash function to compute the hash value of each possible substring of length 5 (the length of the substring “world”) and compare it to the hash value of the target substring “world”.
To compute the hash value of a substring, the Rabin-Karp algorithm uses a rolling hash function that maintains a running hash value of the current substring and updates the hash value as the sliding window moves across the input string.
For instance, the Rabin-Karp rolling hash function might use the following formula to compute the hash value of a substring:
hash(substring) = (c1 * a^(k-1) + c2 * a^(k-2) + … + ck * a^0) mod m where c1, c2, …, ck are the ASCII values of the characters in the substring, a is a prime number (e.g., 31), k is the length of the substring, and m is a large prime number (e.g., 10^9 + 7).

Advantages of the rolling hash algorithm:

Speed: Rolling hash is very fast and efficient in calculating the hash value of a substring. It is especially useful when dealing with large strings, where calculating the hash value of the entire string would be too slow.
Memory usage: Rolling hash uses very little memory, as it only needs to store the hash value of the current window and the hash value of the previous window.
Partial matching: Rolling hash allows for partial matching, which means that you can compare two substrings and quickly determine whether they are equal or not. This is useful for string searching and pattern-matching algorithms.
Disadvantages of the rolling hash algorithm:

Hash collisions: Rolling hash can produce hash collisions, which means that two different substrings can have the same hash value. This can lead to false matches and incorrect results.
Window size: Rolling hash requires a fixed window size, which means that it may not be suitable for all types of strings. If the window size is too small, it may miss important features of the string. If the window size is too large, it may be too slow and memory-intensive.
Limited hash space: Rolling hash has a limited hash space, which means that there is a finite number of hash values that can be generated. This can limit the accuracy and reliability of the hash function.

Note that if two strings are equal, their hash values should also be equal. But the inverse need not be true.
"""

"""
Polynomial Rolling Hash function

hash(s) = s[0] + s[1].p + s[2].p^2 + ...+s[n-1]xp^(n-1) mod m
Here s= string input
length of s = n
p = 31 (Prime Number)
p can be 31, 29791, 11111
m = large prime number
m = 10^9 + 7, 10^9 + 9
Output of hash value ranges between 0 and (m-1) inclusive

"""

def generate_hash_of_substring(start_index,end_index,string):
    #Hash = s[0] + s[1]*p + s[2]*p^2 +...s[n-1]*p^(n-1) %m
    p = 31
    m = 10**9 + 7
    p_pow = 1
    calculated_hash = 0
    for i in range(start_index,end_index,1):
        calculated_hash = (calculated_hash + (1 + ord(string[i]) - ord('a'))*p_pow)%m
        p_pow = (p_pow*p)%m
    return calculated_hash