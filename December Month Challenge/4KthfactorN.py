class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        s1 = set()
        s2 = set()
        for i in range(1,int(n**0.5)+1):
            if n%i ==0:
                s1.add(i)
                s2.add(int(n/i))
        l = list(s1|s2)
        l.sort()
        if k > len(l):
            return -1
        return l[k-1]