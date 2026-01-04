class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        N= len(matrix)
        
        for i in range(N-1):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]

        for i in range(N):
            matrix[i] = [matrix[i][j] for j in range(N-1, -1, -1)]


#O(N^2) time and O(1) space
#s1 transpose + reverse each row
#s2 rotate 4 rectangles one by one