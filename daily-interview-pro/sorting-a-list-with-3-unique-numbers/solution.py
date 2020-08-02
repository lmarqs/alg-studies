def sortNums(nums):
    one_idx = 0
    three_idx = len(nums) - 1

    i = 0
    while i <= three_idx:
        if nums[i] == 1:
            nums[i], nums[one_idx] = nums[one_idx], nums[i]
            one_idx += 1
            i += 1 # i can never be lower than one_idx

        elif nums[i] == 2:
            i += 1

        elif nums[i] == 3:
            nums[i], nums[three_idx] = nums[three_idx], nums[i]
            three_idx -= 1

    return nums
