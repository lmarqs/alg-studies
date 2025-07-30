def lookAndSayNth(n):
    ans = "1"
    for _ in range(1, n):
        ans = lookAndSay(ans)
    return ans


def lookAndSay(n):
    ans = ""
    i = 0

    while i < len(n):
        k = n[i]
        c = 1

        while i + c < len(n) and n[i + c] == k:
            c += 1

        ans += str(c) + k
        i += c

    return ans
