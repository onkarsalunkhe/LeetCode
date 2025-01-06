class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        binary_list = [int(digit) for digit in boxes]
        n = len(binary_list)
        
        # Find positions of all 1s
        one_positions = [i for i in range(n) if binary_list[i] == 1]
        
        # Calculate result for each position
        result = []
        for i in range(n):
            # Sum of distances to all 1s from current position
            distance_sum = sum(abs(i - pos) for pos in one_positions)
            result.append(distance_sum)
        
        return result
        