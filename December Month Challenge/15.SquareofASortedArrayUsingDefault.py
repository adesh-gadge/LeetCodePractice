# here sort() uses timsort which takes adavantage of runs of already sorted arrays hence it is faster in this particular case
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,val in enumerate(nums):
            nums[i] = val*val
        nums.sort()
        return nums