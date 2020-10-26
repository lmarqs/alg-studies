from functools import cmp_to_key


def largestNum(nums):
    return ''.join(sorted([str(n) for n in nums], key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1)))