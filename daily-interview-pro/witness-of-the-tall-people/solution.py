def witnesses(heights):
    count = 0
    tallest = 0
    for height in heights[::-1]:
        if height >= tallest:
            tallest = height
            count += 1

    return count

