class Solution(object):
    def validPalin(self,s):
        x= s.lower()
        x=re.sub('[^a-z0-9]','',x)
        for i in range(len(x)/2):
            if x[i]!=x[len(x)-1-i]:
                return False
        return True 
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxPalin=0
        out=''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.validPalin(s[i:j+1]) and len(s[i:j+1])>maxPalin:
                    out=s[i:j+1]
                    maxPalin=len(s[i:j+1])
        return out            
                    
                    
                    
                
                
