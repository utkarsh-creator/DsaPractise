# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getheight(node):
            height=0
            while node:
                height+=1
                node = node.left
            return height
        if not root:
            return 0
        
        left=getheight(root.left)
        right=getheight(root.right)
        count=0
        if left == right:
            # Full tree on the left, so we add 2^left + recurse on right subtree
            return (2 ** left) + self.countNodes(root.right)
        else:
            # Full tree on the right, so we add 2^right + recurse on left subtree
            return (2 ** right) + self.countNodes(root.left)