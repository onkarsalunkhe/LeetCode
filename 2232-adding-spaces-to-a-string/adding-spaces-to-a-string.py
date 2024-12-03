class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # List to store characters (more efficient than string concatenation)
        result = []
        space_index = 0

        for string_index in range(len(s)):
            if (
                space_index < len(spaces)
                and string_index == spaces[space_index]
            ):
                # Insert space at the correct position
                result.append(" ")
                space_index += 1

            # Append the current character
            result.append(s[string_index])

        # Join all characters into final string
        return "".join(result)

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


