def hIndex1(publications):
    p = sorted(publications)
    for i, n in enumerate(p):
        h = len(p) - i
        if n >= h:
            return h
    return 0


def hIndex2(publications):
    histogram = [0] * (1 + len(publications))

    for c in publications:
        histogram[min(len(publications), c)] += 1

    acc = 0
    for h in range(len(histogram) - 1, 0, -1):
        acc += histogram[h]
        if acc >= h:
            return h

    return 0
