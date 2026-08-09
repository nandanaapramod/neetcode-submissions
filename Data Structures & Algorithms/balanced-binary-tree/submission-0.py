# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal=True

        def dfs(root):
            if not root:
                return [True,0]
            leftH=dfs(root.left)
            rightH=dfs(root.right)
            
            bal=leftH[0] and rightH[0] and abs(leftH[1]-rightH[1])<=1

            return [bal,1+max(leftH[1], rightH[1])]
            
        return dfs(root)[0]

