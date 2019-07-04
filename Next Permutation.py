# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        if m <= 1:
            return
        j = m - 2
        while j >= 0 and not nums[j] < nums[j + 1]:
            j -= 1

        # j could be -1 or index
        if j >= 0:
            # 这一步实际上可以使用二分查找！
            e = m - 1
            while nums[e] <= nums[j]:
                e -= 1
            nums[j], nums[e] = nums[e], nums[j]
        l = j + 1
        r = m - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == '__main__':
    a = Solution()
    rst = a.nextPermutation([3,5,6,2,1])
    print(rst)

