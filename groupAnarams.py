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
            print('key:',key)
            if key not in dicts:
                dicts[key]= j
                print(dicts)
                out.append([i])
                j+=1
                print('out ',out)
                
            else:
                out[dicts[key]].append(i)
                print('out ',out)
        print(dicts)        
        return out
                
            
            
