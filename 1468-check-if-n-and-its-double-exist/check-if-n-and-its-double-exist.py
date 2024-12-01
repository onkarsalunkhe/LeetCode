class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        while(len(arr)>=2):
            if (arr[0]>0 and arr[0]*2 in arr[1:]):
                return True
            if (arr[0]<=0 and arr[0]/2 in arr[1:]):
                return True
            arr.pop(0)
        return False