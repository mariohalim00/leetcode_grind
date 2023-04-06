# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left
            tmp = stack.pop()
            res.append(tmp.val)
            curr = tmp
            curr = curr.right

        return res

            
        # res = []
        # def inorder(root: Optional[TreeNode]):
        #     if(root == None): return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return res