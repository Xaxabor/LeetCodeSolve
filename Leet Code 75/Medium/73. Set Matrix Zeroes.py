class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        s = set()
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    s.add("r"+str(i))
                    s.add("c"+str(j))

        for i in range(m):
            for j in range(n):
                if "r"+str(i) in s or "c"+str(j) in s:
                    matrix[i][j]=0


#O(MN) Time  O(M+N) space
# first iteration use a set to store the zeros row r1 and culumn c1
# then second iteration for each cordinate if that cordinate's row or column in set then set 0