def matrix_spiral_print(M, depth=0):
    top = depth
    bottom = len(M) - 1 - depth

    if top > bottom:
        return ""

    ans = ""

    left = depth
    right = len(M[top]) - 1 - depth

    for i in range(left, right):
        ans += " " + str(M[top][i])

    for i in range(top, bottom + 1):
        ans += " " + str(M[i][right])

    for i in range(right - 1, left - 1, -1):
        ans += " " + str(M[bottom][i])

    for i in range(bottom - 1, top, -1):
        ans += " " + str(M[i][left])

    return (ans + " " + matrix_spiral_print(M, depth + 1)).lstrip().rstrip()
