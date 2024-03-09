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
    


def string_properties(strng=None):
    '''String Properties'''
    strng = 'GeeksforGeeks'
    print(f"split string characters and store in list")
    letters = [x for x in strng]
    letters = ['G','e','e','k','s','f','o','r','G','e','e','k','s']
    sorted(strng)
