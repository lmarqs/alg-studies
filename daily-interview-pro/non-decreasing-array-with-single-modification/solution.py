def check(lst):
    count = 0
    highest = lst[0]

    for i in range(1, len(lst)):
        current = lst[i]

        if current >= highest:
            highest = current
            continue

        count += 1
        if count >= 1:
            return False

        # reseting highest
        if i == 1:
            highest = current
        elif current >= lst[i - 2]:
            highest = lst[i - 2]

    return True
