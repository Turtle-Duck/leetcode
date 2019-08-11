# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest_core(self, node, k):
        if not node:
            return 0, 0
        l_sum, l_rst = self.kthSmallest_core(node.left, k)
        if l_sum == -1:
            return -1, l_rst
        if l_sum + 1 == k:
            return -1, node.val
        r_sum, r_rst = self.kthSmallest_core(node.right, k - l_sum - 1)
        if r_sum == -1:
            return -1, r_rst
        return l_sum + r_sum + 1, 1

    def kthSmallest(self, root, k):
        if not root:
            return -1
        else:
            _, rst = self.kthSmallest_core(root, k)
        return rst


if __name__ == '__main__':
    a = Solution()
    p = TreeNode(3)
    p.left = TreeNode(1)
    p.right = TreeNode(4)
    p.left.right = TreeNode(2)
    rst = a.kthSmallest_core(p, 1)
    print(rst)
