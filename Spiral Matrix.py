# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


def spiralOrder(matrix):
    # print(matrix)
    # print([*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1]))
    # print(matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1]))
    # exit()

    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])


if __name__ == '__main__':
    a = spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]])
    print(a)
