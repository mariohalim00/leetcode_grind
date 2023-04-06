# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []
        stack = [root]
        curr = root
        
        while(stack):
            # print(stack)
            if(curr):
                # print(f'curr {curr.val}')
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                arr.append(node.val)
                curr = node.right
        print(arr)
        return arr[k-1]