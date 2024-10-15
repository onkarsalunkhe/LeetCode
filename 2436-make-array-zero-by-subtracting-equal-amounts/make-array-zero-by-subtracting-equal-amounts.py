class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        myset = set(nums)
        count = 0
        for i in myset:
            if i>0:
                count +=1
        return count
        