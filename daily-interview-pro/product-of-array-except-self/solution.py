def products1(nums):
    res = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                res[i] *= nums[j]

    return res


def products2(nums):

    prefix_products = [1]
    for i in range(len(nums)):
        prefix_products = prefix_products + [prefix_products[-1] * nums[i]]

    suffix_products = [1]
    for i in range(len(nums) - 1, 0, -1):
        suffix_products = [suffix_products[0] * nums[i]] + suffix_products

    return [a * b for a, b in zip(prefix_products, suffix_products)]
