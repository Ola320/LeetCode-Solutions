# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        stack, output = [root], []

        while stack:
            current = stack.pop()

            if current:
                output.append(current.val)

                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

        return output