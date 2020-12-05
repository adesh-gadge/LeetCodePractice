class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        i = 0
        prev = 0
        while(i < len(flowerbed)):
            if i+1 == len(flowerbed):
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    cnt+=1
                    if cnt >= n :
                        return True
                i+=1
                continue  
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                cnt+=1
                i+=1
                if cnt >= n :
                    return True
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[0]=1
                cnt+=1
                if cnt >= n :
                    return True   
            
            i+=1
        return cnt >= n