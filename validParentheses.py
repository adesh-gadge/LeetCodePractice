class Solution(object):
    
    def isValidPair(self,a,b):
        pairs= { '{':'}', '(':')','[':']'}
        return pairs[a]==b
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #stack
        l=[]
        for i in range(len(s)):
            if s[i] in ('{','(','['):
                l.append(s[i])
            else:
                if len(l)!=0:
                    a=l.pop()
                    if not(self.isValidPair(a,s[i])):
                        return False
                else:
                    return False
        if len(l)!=0:
            return False
        return True        
                
                
