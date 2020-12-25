class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        l=len(matrix)
        b= len(matrix[0])
        ans = [[] for i in range(l+b-1)]
        for i in range(l):
            for j in range(b):
                ans[i+j].append(matrix[i][j])
        result = []        
        for i in range(len(ans)):
            if i%2 ==0:
                ans[i]= ans[i][::-1]
            result.extend(ans[i])
        return result