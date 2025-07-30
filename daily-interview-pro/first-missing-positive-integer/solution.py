def first_missing_positive(nums):
    if not nums:
        return 1

    i = 0
    while i < len(nums):
        j = i
        while nums[j] in range(len(nums)) and nums[j] != j:
            nums[nums[j]], nums[j] = nums[j], nums[nums[j]]
        i += 1

    for i, num in enumerate(nums[1:], 1):
        if num != i:
            return i

    return len(nums)
