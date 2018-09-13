# -*- coding = utf-8 -*-
import sys


def getHeart(x1, y1, x2, y2):
    ans = [["-"] * 10 for _ in range(10)]
    ans[x1][y1] = "#"
    ans[x2][y2] = "#"
    ans[x1 + 1][y1 - 1:y2 + 2] = "#" * 7
    ans[x1 + 1][(y1 + y2)//2] = "-"
    ans[x1 + 2][y1 - 2:y2 + 2] = "#" * 9
    ans[x1 + 3][y1 - 1:y2 + 2] = "#" * 7
    ans[x1 + 4][y1: y2 + 1] = "#" * 5
    ans[x1 + 5][y1 + 1 : y2 - 1] = "#" * 3
    ans[x1 + 6][(y1 + y2)//2] = "#"
    return ans



if __name__ == "__main__":
    xy = sys.stdin.split()
    x1 = xy[0] - 1
    y1 = xy[1] - 1
    x2 = xy[2] - 1
    y2 = xy[3] - 1
    x1 = 2
    y1 = 3
    x2 = 2
    y2 = 7
    ans = getHeart(x1, y1, x2, y2)
    for line in ans[:10]:
        print(" ".join(i) for i in line[:10])
