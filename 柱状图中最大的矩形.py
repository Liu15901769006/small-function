# -*- coding = utf-8 -*-


def largestRectangleArea(height):
    """
    :type height:list
    :rtype:int
    """
    if not height:
        return 0
    height.append(-1)
    stack = []
    ans = 0
    for i in range(0, len(height)):
        while stack and height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1 if stack else i
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans


if __name__ == "__main__":
    height = [2, 1, 5, 6, 2, 3]
    ans = largestRectangleArea(height)
    print(ans)