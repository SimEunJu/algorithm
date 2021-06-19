# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def findDepthDfs(node):
            if not node:
                return 0
            
            leftDepth = findDepthDfs(node.left) + 1
            rightDepth = findDepthDfs(node.right) + 1
            
            return max(leftDepth, rightDepth)
        
        return findDepthDfs(root)
