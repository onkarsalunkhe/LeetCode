class Solution:
    def rotate_matrix(matrix):
        # Transpose the matrix
        transposed = list(zip(*matrix))

        # Reverse each row of the transposed matrix
        rotated = [list(reversed(row)) for row in transposed]

        return rotated

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row = len(box)
        col = len(box[0])
        for i in range(row):
            # flag = -1
            # start = -1
            for j in range(col):
                if (box[i][j] == "#"):
                    start = j
                    end = j
                    while end<col and  box[i][end] == "#":
                        end+=1
                    
                    if end<col and box[i][end] == ".":
                        temp = box[i][end]
                        box[i][end] = box[i][start]
                        box[i][start] = temp
                


                #     if (flag == 1):
                #         continue
                #     else:
                #         flag = 1
                #         start = j
                # if (box[i][j] == "."):
                #     if (start >= 0):
                #         box[i][j]="#"
                #         box[i][start] = "."
                #         flag = 0
                #         start = -1
                # if (box[i][j] == "*"):
                #     flag = 0
                #     start = -1
        
        return Solution.rotate_matrix(box)
