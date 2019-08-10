# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
import copy


class Solution:

    def rec_test(self, s, rst, rcd, temp, start, m):
        if start == m:
            rst.append(temp)
            return
        for t in range(m - start):
            # index: start, t+start
            if rcd[start][start + t]:
                new_temp = copy.copy(temp)
                new_temp.append(s[start:start + t + 1])
                self.rec_test(s, rst, rcd, new_temp, start + t + 1, m)

    def partition(self, s: str):
        m = len(s)
        if m < 1:
            return []
        rcd = [[False for i in range(m)] for j in range(m)]
        for i in range(m):
            rcd[i][i] = True
        for i in range(m - 1):
            rcd[i + 1][i] = True
        for t in range(m - 1):
            for j in range(m - 1 - t):
                # index: j, t+j+1
                if rcd[j + 1][t + j] and s[j] == s[t + j + 1]:
                    rcd[j][t + j + 1] = True
        rst = []
        for i in range(m):
            if rcd[0][i]:
                temp = [s[0:i + 1]]
                self.rec_test(s, rst, rcd, temp, i + 1, m)

        return rst

    def partition_1(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    a = Solution()
    rst = a.partition_1("abacc")
    print(rst)
