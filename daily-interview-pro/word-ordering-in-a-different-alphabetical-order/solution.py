def isSorted(words, order):

    order_map = {}
    for i in range(len(order)):
        order_map[order[i]] = i

    for i in range(1, len(words)):
        w1, w2 = words[i - 1], words[i]
        diff = False

        for j in range(min(len(w1), len(w2))):
            comparation = order_map[w1[j]] - order_map[w2[j]]

            if comparation > 0:
                return False

            diff = comparation != 0
            if diff:
                break

        if not diff and len(w1) > len(w2):
            return False

    return True
