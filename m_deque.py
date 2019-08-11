import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []

        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()

            d.append(i)
            if d[0] == i - k:  # 存了K+1个元素了
                d.popleft()
            if i >= k - 1:
                out.append(nums[d[0]])
        return out

    def sumSubarrayMins(self, A):
        # res = 0
        # stack = []  # non-decreasing
        # A = [float('-inf')] + A + [float('-inf')]
        # for i, n in enumerate(A):
        #     while stack and A[stack[-1]] > n:
        #         cur = stack.pop()
        #         res += A[cur] * (i - cur) * (cur - stack[-1])
        #     stack.append(i)
        # return res % (10 ** 9 + 7)

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    a = Solution()
    rst = a.maxSlidingWindow([1,3,1,2,0,5], 3)
    print(rst)
    print(a.sumSubarrayMins([3,1,2,4]))


