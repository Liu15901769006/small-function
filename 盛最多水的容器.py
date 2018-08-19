# -*- coding = utf-8 -*-


def maxArea(height):
    """
    :type height:list
    :rtype:int
    """
    head = 0
    tail = len(height) - 1
    max_water = 0
    while head < tail:
        max_water = max(max_water, min(height[head], height[tail]) * (tail - head))
        if height[head] < height[tail]:
            head += 1
        else:
            tail -= 1
    return max_water


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = maxArea(height)
    print(ans)
