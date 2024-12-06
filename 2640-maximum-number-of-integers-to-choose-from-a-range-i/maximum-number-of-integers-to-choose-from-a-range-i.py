class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        my_list = list(range(1, n + 1))
        print(my_list) 
        banned = list(set(banned))
        for b in banned:
            if b<=n:
                my_list.remove(b)

        sum = 0
        k=0
        for i in range(len(my_list)):
            k+=1
            sum += my_list[i]
            if (maxSum < sum):
                return i

        if (k==len(my_list)):
            return k

        return 0





 