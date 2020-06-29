class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=''
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if len(m)> j-i:
                    break
                elif s[i:j]==s[i:j][::-1]:
                    m=s[i:j]
        return m            
                    
                    
        
