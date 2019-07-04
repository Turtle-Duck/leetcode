# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        l_r_map = {'(': ')', '{': '}', '[': ']'}
        ss = list()
        for c in s:
            if c in left:
                ss.append(c)
            else:
                if len(ss) == 0:
                    return False
                temp = ss.pop()
                if l_r_map[temp] != c:
                    return False
        if len(ss) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    rst = a.isValid("()")
    print(rst)



