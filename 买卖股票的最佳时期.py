# -*- coding = utf-8 -*-


def maxProfit(prices):
    """
    :type prices:list
    :rtype:int
    """
    maxsum = 0
    cursum = 0
    for i in range(1, len(prices)):
        cursum = max(0, cursum + prices[i] - prices[i - 1])
        maxsum = max(cursum, maxsum)
    return maxsum


if __name__ == "__main__":

    prices = [7, 1, 5, 3, 6, 4]
    ans = maxProfit(prices)
    print(ans)

    prices = [7, 6, 4, 3, 1]
    ans = maxProfit(prices)
    print(ans)