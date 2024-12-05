class Solution:
    # def canChange(self, start: str, target: str) -> bool:
    #     combo1 = []
    #     combo2 = []
    #     spaceR = 0
    #     spaceL = 0
        
    #     for i in target:
    #         if i == "_":
    #             space2 += 1
    #         else:
    #             combo2.append(i)

    #     for i in start:
    #         if i == "_":
    #             space1 += 1
    #         else:
    #             combo1.append(i)
        
    #     if combo1 == combo2 and space1==space2:
    #         return True
    #     return False

    # class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        waitL = 0   
        waitR = 0    

        for curr, goal in zip(start, target):
            if curr == 'R':
                if waitL > 0:
                    return False
                waitR += 1  
            if goal == 'L':
                if waitR > 0:
                    return False
                waitL += 1
            if goal == 'R':
                if waitR == 0:
                    return False
                waitR -= 1 
            if curr == 'L':
                if waitL == 0:
                    return False
                waitL -= 1    
        return waitL == 0 and waitR == 0