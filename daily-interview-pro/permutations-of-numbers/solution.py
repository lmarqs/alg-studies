def permute(nums, depth=0):
    if depth == len(nums) - 1:
        return [nums]

    result = permute(nums, depth + 1)

    for i in range(depth + 1, len(nums)):
        nums = nums[:]
        nums[depth], nums[i] = nums[i], nums[depth]
        result += permute(nums, depth + 1)

    return result
