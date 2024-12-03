class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # List to store characters (more efficient than string concatenation)
        res = []
        space_idx = 0

        for i in range(len(s)):
            if (space_idx<len(spaces) and i==spaces[space_idx]):
                res.append(' ')
                space_idx += 1
            res.append(s[i])
        
        res = ''.join(res)
        return str(res)

        # k = 0
        # while len(spaces)>0:
        #     k+=1
        #     idx = spaces[0]
        #     print(s[:idx])
        #     s = s[:idx] + ' ' + s[idx:]
        #     spaces.pop(0)
        #     if len(spaces)>0:
        #         spaces[0] += k
        #         print(spaces)
        # return s


