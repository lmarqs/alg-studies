def singleNumber1(nums):
    if len(nums) == 0:
        return nums[0]

    nums.sort()

    for i in range(len(nums)):
        if i == 0 and nums[i] != nums[i + 1]:
            return nums[i]
        elif i == len(nums) - 1 and nums[i] != nums[i - 1]:
            return nums[i]
        elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]


def singleNumber2(nums):
    unique = 0
    for n in nums:
        unique ^= n
    return unique
