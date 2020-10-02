def findRanges(nums):
    ranges = []

    if len(nums) < 0:
        return ranges

    low = high = nums[0]

    for n in nums:
        if n > high + 1:
            ranges.append("%s->%s" % (low, high))
            low = high = n
            continue

        high = n

    ranges.append("%s->%s" % (low, high))

    return ranges
