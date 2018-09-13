# -*- coding = utf-8 -*-


def groupAnagrams(strs):
    """
    :type strs:list
    :rtype:list
    """
    def hash(count):
        p1 = 2903
        p2 = 29947
        ret = 0
        for c in count:
            ret = ret * p1 + c
            p1 *= p2
        return ret
    d = {}
    for str in strs:
        count = [0] * 26
        for c in str:
            count[ord(c) - ord("a")] += 1
            key = hash(count)
        if key not in d:
            d[key] = [str]
        else:
            d[key].append(str)
    return [d[k] for k in d]


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = groupAnagrams(strs)
    print(ans)
