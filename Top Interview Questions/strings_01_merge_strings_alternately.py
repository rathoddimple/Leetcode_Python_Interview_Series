class Solution:
    
        def __init__(self,word1,word2):
            self.word1 = word1
            self.word2 = word2
    
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

        