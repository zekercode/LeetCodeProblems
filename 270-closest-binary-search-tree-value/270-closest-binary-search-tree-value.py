# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        current = root
        
        while current:
            if current.val == target:
                closest = current.val
                break
            elif abs(current.val - target) < abs(closest - target):
                closest = current.val
            elif target < current.val:
                current = current.left
            else:
                current = current.right
        return closest