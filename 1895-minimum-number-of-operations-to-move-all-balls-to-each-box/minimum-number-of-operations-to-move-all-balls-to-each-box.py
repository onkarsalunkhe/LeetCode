class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        # Find positions of all '1's in the binary string
        one_positions = [i for i in range(n) if boxes[i] == '1']
        
        # If there are no '1's or only one '1', distances will be zero for all
        if len(one_positions) == 0:
            return [0] * n
        
        result = [0] * n
        
        # For each '1' at position `i`, calculate the sum of distances to all other '1's
        for i in range(n):
            if boxes[i] == '1':
                # Sum the distance to each other '1'
                result[i] = sum(abs(i - pos) for pos in one_positions if pos != i)
            else:
                # For each '0', calculate the sum of distances to all '1's
                result[i] = sum(abs(i - pos) for pos in one_positions)
        
        return result