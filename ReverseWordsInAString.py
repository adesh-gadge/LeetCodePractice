class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        words=s.split()
        
        for i in range(len(words)):
            ans+=words[len(words)-1-i]
            if i!=len(words)-1:
                ans+=' '
        return ans
    
    # or     return " ".join(reversed(s.split()))     
