class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # (a+b) mod n = [a mod n + b mod n] mod n
        # so (a+b) mod n = 0 means  (1) a mod n =0 and b mod n = 0 or (2) a mod n + b mod n = n
        d = collections.defaultdict(int)
        cnt = 0
        for i in range(len(time)):
            
            if time[i]% 60 == 0:
                cnt += d[0] 
            else: 
                cnt += d[60-(time[i])%60]
            d[time[i]%60] +=1
        return cnt
            