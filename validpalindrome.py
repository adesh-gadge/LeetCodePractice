class Solution:
    def isPalindrome(self, s: str) -> bool:        
        x=""
        for i in range(len(s)):
            if s[i].isalnum():
                x+=s[i]
        x=x.lower()
        x = re.sub('[^a-z0-9]','',x)
        for i in range(int(len(x)/2)):
            if x[i]!=x[len(x)-i-1]:
                return False
        return True    
    
    
    
    
            
            
