# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


class Solution:
    def letterCombinations(self, digits):
        mm = [3, 3, 3, 3, 3, 4, 3, 4]
        mm1 = ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w']
        m = len(digits)
        if m == 0:
            return []
        count = [0 for i in range(m)]
        rst = []
        all_num = pow(3, m)
        stop = False

        while not stop:
            temp = ''
            for j in range(m):
                temp += chr(ord(mm1[int(digits[j]) - 2]) + count[j])
            rst.append(temp)
            j = m - 1
            count[j] += 1
            while j >= 0 and count[j] == mm[int(digits[j]) - 2]:
                count[j] = 0
                if j > 0:
                    count[j - 1] += 1
                else:
                    stop = True
                j -= 1

        return rst


class Solution1:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]


if __name__ == '__main__':
    a = Solution1()
    rst = a.letterCombinations('23')
    print(rst)
