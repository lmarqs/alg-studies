def findPythagoreanTriplets(nums):
    results = set()
    nums.sort()
    for i in range(len(nums) - 2):
        results.add(nums[i] ** 2 + nums[i + 1] ** 2)
        if nums[i + 2] ** 2 in results:
            return True

    return False
