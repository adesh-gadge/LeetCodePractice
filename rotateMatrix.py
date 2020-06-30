class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose 
        n= len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[j][i],matrix[i][j]= matrix[i][j],matrix[j][i]
                
        # REVERSE EACH ROW
        for i in range(n):
            matrix[i].reverse()
