# -*- coding = utf-8 -*-


def rotate(matrix):
    """
    :type matrix: list
    :rtype:void do not return anything, modify matrix in-place instead
    """
    if len(matrix) == 0:
        return
    h = len(matrix)
    w = len(matrix[0])
    for i in range(0, h):
        for j in range(0, w // 2):
            be = matrix[i][j]
            matrix[i][j] = matrix[i][w - j - 1]
            matrix[i][w - j - 1] = be
    for i in range(0, h):
        for j in range(0, w - 1 - i):
            be = matrix[i][j]
            matrix[i][j] = matrix[w - 1 - j][h - 1 - i]
            matrix[w - 1 -j][h - 1 - i] = be
    # for i in range(0, h):
    #     for j in range(0, w):
    #         be = matrix[i][j]
    #         matrix[i][j] = matrix[j][w - 1 - j]
    #         matrix[j][w - 1 - j] = be


if __name__ == "__main__":
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(nums)
    print(nums)

    nums = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(nums)
    print(nums)