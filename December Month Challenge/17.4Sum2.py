class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d1={}
        ans=0
        for i in range(len(A)):
            for j in range(len(B)):
                if -(A[i]+ B[j]) not in d1:
                    d1[-(A[i]+B[j])]=1
                else: 
                    d1[-(A[i]+B[j])]+=1
        for i in range(len(C)):
            for j in range(len(D)):
                if C[i]+D[j] in d1:
                    ans += d1[C[i]+D[j]]
        return ans
                
                    
                    