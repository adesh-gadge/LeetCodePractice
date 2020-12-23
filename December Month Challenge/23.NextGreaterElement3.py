from struct import pack, error 
class Solution:
    def smallGreatNextSwap(self,l):
        for i in range(len(l)-1,0,-1):
            if l[i]>l[0]:
                temp = l[i]
                l[i] = l[0]
                l[0] = temp
                break
        return l
         
        
    #
    def nextGreaterElement(self, n: int) -> int:
        l = [int(i) for i in str(n)]
        prev = -1
        for i in range(len(l)-1,-2,-1):
            if l[i] < prev or i ==-1:
                break                
            prev = l[i]
        if i == -1:
            return -1
        l[i:] = self.smallGreatNextSwap(l[i:])
        l[i+1:] = sorted(l[i+1:])
        
        ans = ''
        for v in l:
            ans+=str(v)
        try:
             pack("i", int(ans))
        except error:
            return -1
        
        return int(ans)