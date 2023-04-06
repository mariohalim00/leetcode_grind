# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

# Iterative DFS (preorder)
        res = 0

        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


# BFS Iterative
        # if(root == None): return 0

        # queue = deque([root])
        # level = 0
        # while(queue):
        #     for i in range(len(queue)):
        #         tmp = queue.popleft()
        #         if(tmp.left):
        #             queue.append(tmp.left)
        #         if(tmp.right):
        #             queue.append(tmp.right)
        #     level += 1
        # return level


# RECURSIVE DFS
        # if(root == None): return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
