# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {
            val: i
            for i, val in enumerate(inorder)
        }
        p_idx = 0
        def build(l, r):
            nonlocal p_idx
            if l > r:
                return
            
            val = preorder[p_idx]
            node = TreeNode(val)

            mid = inorder_map[val]
            p_idx += 1

            node.left = build(l, mid-1)
            node.right = build(mid+1, r)
            
            return node

        
        return build(0, len(preorder)-1)




