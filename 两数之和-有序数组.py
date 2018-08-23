# -*- coding = utf-8 -*-
# 解题思路：遍历列表元素时， 创建一个字典，key是列表元素，value是对应索引，创建变量sub，等于目标值减去当前列表元素，
# 判断条件是：如果sub存在字典key中，可以输出字典中对应索引+1和当前列表元素索引+1，否则将该元素按照相应格式存入字典中

def twoSum(numbers, target):
    """
    :type numbers: list
    :type target: int
    :rtype:list
    """
    res = dict()
    for i in range(0, len(numbers)):
        sub = target - numbers[i]
        if sub in res.keys():
            return [res[sub] + 1, i + 1]
        else:
            res[numbers[i]] = i
    return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    ans = twoSum(numbers, target)
    print(ans)
