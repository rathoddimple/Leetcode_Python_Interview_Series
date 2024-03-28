def switch(array,index_1,index_2):
    """switching elements"""
    temp = array[index_1]
    array[index_1] = array[index_2]
    array[index_2] = temp

def list_properties(nums=None):
    '''List Properties'''
    nums = [0,1,2,3]
    for i in range(0,len(nums)):
        print(f"Prints all elements")
        print(f"Length = 3")
        print(f"Index starts from 0")
    print(f"Appending to list")
    nums.append(3)
    print(f"Deleting element from 2nd index from list")
    del nums[2]
    print(f"Creating copy of list")
    nums_copy = nums.copy()
    a = ("h", "b", "a", "c", "f", "d", "e", "g")
    x = sorted(a, reverse=True)
    list = [1]
    list_2 = [1,2]
    list.extend(list_2)
    '''list == [1,1,2]'''
    list.append(list_2)
    '''list == [1, [1,2]]'''
    '''list = [1,2,1,3,4]'''
    list2 = [1,2,1,3,4]
    print(list2.index(1,1))
    """Returns index number 2 --Checking for index of element 1 after index 0"""
    


def string_properties(strng=None):
    '''String Properties'''
    strng = 'GeeksforGeeks'
    print(f"split string characters and store in list")
    letters = [x for x in strng]
    letters = ['G','e','e','k','s','f','o','r','G','e','e','k','s']
    sorted(strng)
    #ord() function in Python is used to convert a single Unicode character into its integer representation, i.e., it takes a single string character as an input and returns an integer (representing the Unicode equivalent of the character) as an output.
    #ord() function returns an error if the length of the string is not equal to 1.
    print(ord('a'))
     

def dict_properties(dct=None):
    """Print dict key,val"""
    for key,val in dct.items():
        print(f"Key {key}")
        print(f"Val {val}")     
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

"""