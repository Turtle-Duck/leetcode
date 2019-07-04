# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1


class Solution:
    def firstMissingPositive(self, nums):
        l = len(nums)
        rst = l + 1
        for i in range(l):
            temp = nums[i]
            # nums[i] = -1
            while temp > 0 and temp - 1 < l and temp - 1 != i and temp != nums[temp - 1]:
                ttt = nums[temp - 1]
                nums[temp - 1] = temp
                temp = ttt
            nums[i] = temp
            # print(nums)
        for i in range(l):
            if nums[i] != i+1:
                rst = i + 1
                break
        return rst


if __name__ == '__main__':
    a = Solution()
    rst = a.firstMissingPositive([2,1])
    print(rst)