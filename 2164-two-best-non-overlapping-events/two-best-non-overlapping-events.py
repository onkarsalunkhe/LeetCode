class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        times = []
        for e in events:
            # 1 denotes start time.
            times.append([e[0], 1, e[2]])
            # 0 denotes end time.
            times.append([e[1] + 1, 0, e[2]])

        ans, max_value = 0, 0
        times.sort()

        for time_value in times:
            # If current time is a start time, find maximum sum of maximum end
            # time till now.
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            else:
                max_value = max(max_value, time_value[2])

        return ans

    #     events.sort(key=lambda x: x[2],reverse=True)
    #     maxVal = 0
    #     numMap = {}
    #     flag =0
    #     stop = len(events)
    #     for i in range(len(events)):
    #         j=i+1
    #         maxVal = max(maxVal,events[i][2])
    #         if (i>=stop): break
    #         while j<len(events):
    #             if (Solution.doOverlap(self,events[i],events[j])):
    #                 j+=1
    #             else:
    #                 if (flag == 0):
    #                     stop = j
    #                     flag = 1
    #                 newVal = events[i][2]+events[j][2]
    #                 j+=1
    #                 if (newVal>=maxVal):
    #                     maxVal = newVal
    #                 break
    #         # if (events[i][2]>maxVal):
    #         #     maxVal = max(maxVal,events[i][2])
    #         # else:
    #         #     break



    #     return maxVal
        
    # def doOverlap(self, eve1:List[int],eve2:List[int]) -> bool:
    #     if ((eve1[0]<eve2[0] and eve1[1]< eve2[0])
    #             or
    #             (eve1[0]>eve2[1] and eve1[1]>eve2[1])):
    #         return False
    #     return True
