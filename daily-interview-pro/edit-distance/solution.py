def distance(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1

    D = [[max(i, j) if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                D[i][j] = D[i - 1][j - 1]

            else:
                D[i][j] = 1 + min(D[i - 1][j - 1], D[i - 1][j], D[i][j - 1])

    return D[-1][-1]
