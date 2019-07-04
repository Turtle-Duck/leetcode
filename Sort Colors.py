# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
#
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pass:
        # m = len(nums)
        # l = 0
        # r = m - 1
        # while l < r:
        #     while l < m and nums[l] < 2:
        #         l += 1
        #     while r >= 0 and nums[r] == 2:
        #         r -= 1
        #     if l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #     else:
        #         break
        #
        # l = 0
        # while l < r:
        #     while l < m and nums[l] < 1:
        #         l += 1
        #     while r >= 0 and nums[r] == 1:
        #         r -= 1
        #     if l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #     else:
        #         break

        # one pass:
        # m = len(nums)
        # e_0 = 0
        # e_1 = 0
        # s_2 = m - 1
        # while e_1 < s_2:
        #     if nums[e_1] == 0:
        #         nums[e_0], nums[e_1] = nums[e_1], nums[e_0]
        #         e_0 += 1
        #         e_1 += 1
        #     elif nums[e_1] == 1:
        #         e_1 += 1
        #     else:
        #         nums[s_2], nums[e_1] = nums[e_1], nums[s_2]
        #         s_2 -= 1

        # one pass:
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


if __name__ == '__main__':
    a = Solution()
    b = [2, 1, 2, 0, 1]
    a.sortColors(b)
    print(b)

