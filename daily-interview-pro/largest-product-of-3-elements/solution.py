def maximum_product_of_three(lst):
    if len(lst) == 0:
        return 0

    if len(lst) <= 3:
        acc = 1
        for n in lst:
            acc *= n
        return acc

    negative1 = 0
    negative2 = 0

    positive1 = 0
    positive2 = 0
    positive3 = 0

    for n in lst:
        if n < 0:
            if n <= negative1:
                negative2 = negative1
                negative1 = n
                continue
            if n <= negative2:
                negative2 = n
                continue
        else:
            if n >= positive1:
                positive3 = positive2
                positive2 = positive1
                positive1 = n
                continue
            if n >= positive2:
                positive3 = positive2
                positive2 = n
                continue
            if n >= positive3:
                positive3 = n
                continue

    return max(negative1 * negative2 * positive1, positive3 * positive2 * positive1)
