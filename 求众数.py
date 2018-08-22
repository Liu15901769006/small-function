# -*- coding = utf-8 -*-


def majorityElement(num):
    return sorted(num)[int(len(num)/2)]


if __name__ == "__main__":
    num = [3, 2, 3]
    print(majorityElement(num))

    num = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(num))