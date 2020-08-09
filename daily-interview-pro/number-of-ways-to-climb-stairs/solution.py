def staircase(n):
    n1 = 0
    n2 = 1

    for _ in range(n):
        total = n1 + n2
        n1, n2 = n2, total

    return total
