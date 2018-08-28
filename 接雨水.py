# -*- coding = utf-8 -*-


def trap(height):
    """
    :type height:list
    :rtype: int
    """
    ans  = 0
    left = 0
    right = len(height) - 1
    leftWall = float("-inf")
    rightWall = float("-inf")
    while left <= right:
        if leftWall <= rightWall:
            ans += max(0, leftWall - height[left])
            leftWall = max(leftWall, height[left])
            left += 1
        else:
            ans += max(0, rightWall - height[right])
            rightWall = max(rightWall, height[right])
            right -= 1
    return ans


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans = trap(height)
    print(ans)

