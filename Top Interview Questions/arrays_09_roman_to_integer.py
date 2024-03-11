class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            0: 1,  #I      
            1: 5,  #V
            2: 10, #X
            3: 50, #L
            4: 100, #C
            5: 500, #D
            6: 1000 #M
        }
        ord = ["I","V","X","L","C","D","M"]
        int_val = 0
        i = len(s) - 1
        while i > -1:
            if i == 0:
                int_val+=mapping[int(ord.index(s[i]))]
                i-=1
            else:
                if ord.index(s[i-1]) == (ord.index(s[i]) - 2) or ord.index(s[i-1]) == (ord.index(s[i]) - 1):
                    print("inside subs")
                    add = mapping[int(ord.index(s[i]))] - mapping[int(ord.index(s[i-1]))]
                    i-=2
                else:
                    add = mapping[int(ord.index(s[i]))]
                    i-=1
                int_val +=add
        return int_val
obj = Solution()
int_val = obj.romanToInt("MCMXCIV")
print(f"Int Value {int_val}")