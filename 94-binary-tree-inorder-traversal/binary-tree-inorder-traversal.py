# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node:Optional[TreeNode])->List[int]:
            if node is None:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        return inorder(root)
        