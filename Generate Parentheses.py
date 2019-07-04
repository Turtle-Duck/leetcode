# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution_wrong:
    # Wrong for (())(())
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        rst = set(['()'])
        for i in range(n - 1):
            temp = set()
            for r in rst:
                temp.add('()' + r)
                temp.add(r + '()')
                temp.add('(' + r + ')')
            rst = temp
        return list(rst)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        rst = set(['()'])
        for i in range(n - 1):
            temp = set()
            for r in rst:
                # temp.add('()' + r)
                # temp.add(r + '()')
                # temp.add('(' + r + ')')
                for q in range(len(r)):
                    temp.add(r[0:q] + '()' + r[q:])
                temp.add(r + '()')
            rst = temp
        return list(rst)


if __name__ == '__main__':
    a = Solution()
    rst = a.generateParenthesis(3)
    print(rst)

