# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
#
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
#
# Note that the order of those five elements can be arbitrary.
#
# It doesn't matter what values are set beyond the returned length.


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        if r == 0:
            if nums[0] == val:
                return 0
            else:
                return 1
        while l <= r:
            if nums[l] == val:
                while r > l and nums[r] == val:
                    r -= 1
                if r == l:
                    break
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return l


if __name__ == '__main__':
    a = Solution()
    rst = a.removeElement([3, 2, 2, 3], 3)
    print(rst)