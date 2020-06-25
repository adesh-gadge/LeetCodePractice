class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        
        for i in range(len(s)):
            if s[i].isalnum():
                x+=s[i]
        siz=len(x)  
        x=x.lower()
        if siz==0:
            return True
        for i in range(int(siz/2)):
            if x[i]!=x[siz-(i+1)]:
                return False
        
        return True
            
            
