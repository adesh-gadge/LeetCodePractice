class Solution(object):
    def findZeros(self,matrix):
        zeros_row=[]
        zeros_col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros_row.append(i)
                    zeros_col.append(j)
        return zeros_row,zeros_col           
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """   
        zero_row,zero_col=self.findZeros(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row or j in zero_col:
                    matrix[i][j]=0
                    
        
