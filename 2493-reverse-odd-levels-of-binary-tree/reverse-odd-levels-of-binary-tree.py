# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        currlevel = 0

        def dfs(rootleft, rootright, currlevel):

            if(rootleft == None and rootright == None):
                return

            if ( currlevel % 2 == 0 and root.left!=None and root.right!=None):
                temp = rootleft.val
                rootleft.val = rootright.val
                rootright.val = temp
            
            dfs(rootleft.left, rootright.right, currlevel+1)
            dfs(rootright.left, rootleft.right, currlevel+1)


        dfs(root.left, root.right, currlevel)

        return root

        # def reverse_power_two(arr):
        #     for i in range (len(arr)):
        #         if i%2 !=0:
        #             arr[i]=arr[i][::-1]
        #     return arr

        # def create_binary_tree(arr):
        #     if not arr:
        #         return None

        #     def build_tree(i):
        #         if i >= len(arr) or arr[i] is None:
        #             return None
        #         node = TreeNode(arr[i])
        #         node.left = build_tree(2 * i + 1)
        #         node.right = build_tree(2 * i + 2)
        #         return node

        #     return build_tree(0)

        # if not root:
        #     return []

        # subarray = []
        # queue = deque([root])

        # while queue:
        #     levelsize = len(queue)
        #     level = []
        #     while levelsize:
        #         node = queue.popleft()
        #         if(node):
        #             level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         levelsize-=1
        #     subarray.append(level)

        # print( subarray )


        # reverse_power_two(subarray)
        # print(subarray)
        # newroot = create_binary_tree(subarray)

        # return newroot

        





        