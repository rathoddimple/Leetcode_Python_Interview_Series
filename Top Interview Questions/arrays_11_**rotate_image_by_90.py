class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """Transpose Matrix"""
        n = len(matrix[0])
        # print(n)
        for i in range (0,n-1):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # print(matrix)

        #Swap Elements for each row
        swap_length = int(n/2)
        for i in range(0,n):
            for j in range(0,swap_length):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        # print(matrix)



obj = Solution()
# obj.rotate( [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
obj.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])