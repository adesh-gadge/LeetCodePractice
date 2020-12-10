class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1 or len(arr)==2:
            return False
        flag = 0
        prev = arr[0]
        if arr[1] <= prev:
            return False
        if arr[-1] >= arr[-2]:
            return False
        for i in range(1,len(arr)):
            if flag == 0:
                if prev>arr[i]:
                    flag = 1
                    prev = arr[i]
                    continue 
                if prev==arr[i]:
                    return False
                prev = arr[i]
            if flag == 1 :
                if prev<=arr[i]:
                    return False
                prev = arr[i]
        return True