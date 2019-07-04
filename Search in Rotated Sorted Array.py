# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution_old:
    class Solution:

        def s(self, nums, l, r, t):
            if t == nums[l]:
                return l
            if t == nums[r]:
                return r
            if l == r or l == r - 1:
                return -1
            mid_index = int((l + r) / 2)
            mid = nums[mid_index]
            if mid == t:
                return mid_index
            if mid > t:
                return self.s(nums, l, mid_index, t)
            else:
                return self.s(nums, mid_index, r, t)

        def s_r(self, nums, l, r, t):
            if t == nums[l]:
                return l
            if t == nums[r]:
                return r
            if l == r or l == r - 1 or (t < nums[l] and t > nums[r]):
                return -1

            # if t > nums[l]:
            #     bigger = True
            # else:
            #     bigger = False
            mid_index = int((l + r) / 2)
            mid = nums[mid_index]
            if mid == t:
                return mid_index
            if mid > nums[l]:
                if t < nums[r] or t > mid:
                    return self.s_r(nums, mid_index, r, t)
                else:
                    return self.s(nums, l, mid_index, t)
            else:
                if t > nums[l] or t < mid:
                    return self.s_r(nums, l, mid_index, t)
                else:
                    return self.s(nums, mid_index, r, t)

        def search(self, nums, target) -> int:
            m = len(nums)
            if m == 0:
                return -1
            if nums[-1] > nums[0]:
                return self.s(nums, 0, m - 1, target)
            else:
                return self.s_r(nums, 0, m - 1, target)


class Solution:

    def s_r(self, nums, l, r, t):
        if t == nums[l]:
            return l
        if t == nums[r]:
            return r
        if l == r or l == r - 1 or (t < nums[l] and t > nums[r]):
            return -1

        # if t > nums[l]:
        #     bigger = True
        # else:
        #     bigger = False
        mid_index = int((l + r) / 2)
        mid = nums[mid_index]
        if mid == t:
            return mid_index
        if mid > nums[l]:
            if t > nums[l] and t < mid:
                return self.s_r(nums, l, mid_index, t)
            else:
                return self.s_r(nums, mid_index, r, t)
        else:
            if t < nums[r] and t > mid:
                return self.s_r(nums, mid_index, r, t)
            else:
                return self.s_r(nums, l, mid_index, t)

    def search(self, nums, target) -> int:
        m = len(nums)
        if m == 0:
            return -1
        return self.s_r(nums, 0, m - 1, target)

'''

Better ！！！！

Explanation

Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at.

And the adjustment is done by comparing both the target and the actual element against nums[0].

'''


if __name__ == '__main__':
    a = Solution()
    rst = a.search([4,5,6,7,8,1,2,3], 8)
    print(rst)