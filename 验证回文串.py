# -*- coding = utf-8 -*-


def isPalindrome(s):
    """
    :type s:str
    :rtype:bool
    """
    start = 0
    end = len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    s = 'a man, a plan, a canal: Panama'
    ans = isPalindrome(s)
    print(ans)

    s = "race a car"
    ans = isPalindrome(s)
    print(ans)