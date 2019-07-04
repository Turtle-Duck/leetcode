# Example 1:
#
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m < 2:
            return
        d = (m + 1) // 2
        for i in range(d):
            for q in range(i, m-i-1, 1):
                temp = matrix[i][q]
                matrix[i][q] = matrix[m-q-1][i]
                matrix[m-q-1][i] = matrix[m-i-1][m-q-1]
                matrix[m-i-1][m-q-1] = matrix[q][m-i-1]
                matrix[q][m - i - 1] = temp


if __name__ == '__main__':
    a = Solution()
    b = [[1,2,3],[4,5,6],[7,8,9]]
    a.rotate(b)
    print(b)


# /*
#  * clockwise rotate
#  * first reverse up to down, then swap the symmetry
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3
# */
# void rotate(vector<vector<int> > &matrix) {
#     reverse(matrix.begin(), matrix.end());
#     for (int i = 0; i < matrix.size(); ++i) {
#         for (int j = i + 1; j < matrix[i].size(); ++j)
#             swap(matrix[i][j], matrix[j][i]);
#     }
# }
#
# /*
#  * anticlockwise rotate
#  * first reverse left to right, then swap the symmetry
#  * 1 2 3     3 2 1     3 6 9
#  * 4 5 6  => 6 5 4  => 2 5 8
#  * 7 8 9     9 8 7     1 4 7
# */
# void anti_rotate(vector<vector<int> > &matrix) {
#     for (auto vi : matrix) reverse(vi.begin(), vi.end());
#     for (int i = 0; i < matrix.size(); ++i) {
#         for (int j = i + 1; j < matrix[i].size(); ++j)
#             swap(matrix[i][j], matrix[j][i]);
#     }
# }