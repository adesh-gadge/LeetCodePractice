# here sort() uses timsort which takes adavantage of runs of already sorted arrays hence it is faster in this particular case
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        k = len(nums)-1
        ans = [0]*len(nums)
        while l <= r:
            left, right = abs(nums[l]),abs(nums[r])
            print(left, ' ', right)
            if left < right:
                ans[k]  =right*right
                
                r-=1
            else:
                ans[k]= left*left
                l+=1
            k-=1
        return ans
                
    