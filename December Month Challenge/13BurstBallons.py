
class Solution:
    def maxCoins(self,nums):
        l = len(nums)
        if(l == 0):
            return 0
        dp = [[0]*l for _ in range(l)]
        for n in range(0,l):
            for i in range(0,l-n):
                j= i+n
                for k in range(i,j+1):
                    leftNum = 1 if i==0 else nums[i-1]
                    rightNum = 1 if j==l-1 else nums[j+1]
                    
                    left =0 if k==i else dp[i][k-1]
                    right = 0 if k==j else dp[k+1][j]
                    
                    dp[i][j]= max(dp[i][j], leftNum*nums[k]*rightNum + left+ right)
        return dp[0][l-1]
                    
                
       

