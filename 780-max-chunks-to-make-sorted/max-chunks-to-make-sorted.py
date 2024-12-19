class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        # my_set = set(range(n + 1)) 
        i=0
        j=0
        while i<len(arr):
            j=i
            while j<len(arr):
                my_set = set(range(i,j+1))
                if set(arr[i:j+1])==my_set:
                    res+=1
                    i=j+1
                    break
                else:
                    j+=1

        return res
                





        # res = 1
        # for i in range(len(arr)-1):
        #     if arr[i+1]>arr[i]:
        #         if (arr[:i] and max(arr[:i])<min(arr[i+1:])):
        #             res+=1

        # return res