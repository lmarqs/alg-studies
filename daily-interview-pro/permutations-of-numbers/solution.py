def permute(nums, depth=0, result=[]):
    if depth == len(nums) - 1:
        result += [nums]
        return

    permute(nums, depth + 1, result)

    for i in range(depth + 1, len(nums)):
        nums = nums[:]
        nums[depth], nums[i] = nums[i], nums[depth]
        permute(nums, depth + 1, result)

    return result
