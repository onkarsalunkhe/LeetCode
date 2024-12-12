class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort(reverse=True)
        res = 0
        while k>0:
                left = int(sqrt(gifts[0]))
                res+=left
                gifts[0] = left
                gifts.sort(reverse=True)
                k-=1

        return sum(gifts)
