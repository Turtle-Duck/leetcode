# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        rst = list()
        cur = root
        while cur is not None:
            if cur.left is None:
                rst.append(cur.val)
                cur = cur.right
            else:
                tt = cur.left
                while tt.right is not None:
                    tt = tt.right
                tt.right = cur
                temp = cur
                cur = cur.left
                temp.left = None
        return rst


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    a = Solution()
    rst = a.inorderTraversal(root)
    print(rst)