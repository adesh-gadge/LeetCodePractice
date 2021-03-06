class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral_co(r1,r2,c1,c2):
            for c in range(c1,c2+1):
                yield r1, c
            for r in range(r1+1,r2+1):
                yield r, c2
            if r1 <r2 and c1 <c2:
                for c in range(c2-1,c1,-1):
                    yield r2,c
                for r in range(r2,r1,-1):
                    yield r,c1
            
            
        if n==0: return []
        ans = [[0]*n for i in range(n)]
        r1 , r2 = 0 , n-1
        c1 , c2 = 0 , n-1
        cnt = 1
        while r1<=r2 and c1 <= c2:
            for r , c in spiral_co(r1,r2,c1,c2):
                ans[r][c]=cnt
                cnt+=1
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return ans
                
    
