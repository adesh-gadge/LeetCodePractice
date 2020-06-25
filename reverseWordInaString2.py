       
class Solution(object):
    def reverse(self, l, left, right):
        #reverse that portion of string in place
        while left<right:
            l[left],l[right]=l[right],l[left]
            left,right= left+1,right-1
        
    def reverse_each_word(self, l):
        # reverse each word
        l.reverse()
        j=0
        for i in range(len(l)):
            if l[i]==" " :
                self.reverse(l,j,i-1)
                j=i+1
            if i==len(l)-1:
                self.reverse(l,j,i)
           
       
            
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_each_word(s)
        print(s)
       
