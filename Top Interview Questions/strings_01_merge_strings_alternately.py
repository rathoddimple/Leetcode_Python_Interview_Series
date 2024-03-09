class Solution:
    
        def __init__(self,word1,word2):
            self.word1 = word1
            self.word2 = word2

        
        def merge(self,new_strn:str,index:int,pointer:int,word1:str,word2:str):
            while index != pointer:
                new_strn = new_strn + word1[index:index+1] + word2[index:index+1]
                index+=1
                self.merge(new_strn,index,pointer,word1,word2)
            return new_strn

        def mergeAlternately_old(self) -> str:
            if len(self.word1) != len(self.word2):
                if len(self.word1) > len(self.word2):
                    pointer = len(self.word2)
                    base_string = self.merge('',0,pointer,self.word1,self.word2)
                    return base_string + self.word1[pointer:]

                else:
                    pointer = len(self.word1)
                    base_string = self.merge('',0,pointer,self.word1,self.word2)
                    return base_string + self.word2[pointer:]
            else:
                pointer = len(self.word1)
                return self.merge('',0,pointer,self.word1,self.word2)
            
        def mergeAlternately(self) -> str:
            pointer = min(len(self.word1),len(self.word2))
            base_strn = ''
            for i in range(pointer):
                base_strn += self.word1[i:i+1] + self.word2[i:i+1]
            if len(self.word1) == len(self.word2):
                return base_strn
            if len(self.word1) > len(self.word2):
                return base_strn + self.word1[pointer:]
            else:
                return base_strn + self.word2[pointer:]

if __name__ == '__main__':
    obj = Solution("abc","pqrs")
    merged_string = obj.mergeAlternately()
    print(f"Merged string {merged_string}")

        