class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts={}
        out=[]
        j=0
        for i in strs:
            key=''.join(sorted(i))
            if key not in dicts:
                dicts[key]= j
                
                out.append([i])
                j+=1
                
                
            else:
                out[dicts[key]].append(i)
                
        
        return out
                
