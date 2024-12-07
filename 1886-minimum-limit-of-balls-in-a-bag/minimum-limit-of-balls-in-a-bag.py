class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # while maxOperations>0:
        #     nums.sort()
        #     n1 = int(nums[-1]/2)
        #     n2 = nums[-1]-n1
        #     nums.pop()
        #     nums.append(n1)
        #     nums.append(n2)
        #     nums.sort()
        #     maxOperations-=1
        # return nums[-1]

        low, high = 1, max(nums) # min and max posible bags
        while low < high:
            mid = (low + high) // 2
            if sum((n - 1) // mid for n in nums) <= maxOperations: high = mid
            else: low = mid + 1
        return high
