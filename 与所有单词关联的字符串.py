# -*- coding = utf-8 -*-


def findSubstring(s, words):
    """
    :type s: str
    :type words: list
    :rtype: list
    """
    sum = 0
    for word in words:
        sum += len(word)
    if sum > len(s):
        return []

    d = {}
    t = {}
    ans = []
    wl = len(words[0])
    fullscore = 0
    for word in words:
        d[word] = d.get(word, 0) + 1
        fullscore += 1
    for i in range(0, len(s)):
        head = i
        start = i
        t.clear()
        score = 0
        while start + wl <= len(s) and s[start:start + wl] in d:
            cword = s[start:start + wl]
            t[cword] = t.get(cword, 0) + 1
            if t[cword] <= d[cword]:
                score += 1
            else:
                break
            start += wl
        if score == fullscore:
            ans.append(head)
    return ans


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    ans = findSubstring(s, words)
    print(ans)

    s = "wordgoodstudentgoodword"
    words = ["word","student"]
    ans = findSubstring(s, words)
    print(ans)
