class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k>0:
            minval = min(nums)
            idx = nums.index(minval)
            nums[idx] = nums[idx]*multiplier
            k-=1
        return nums