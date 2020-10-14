# Kadane's Algorithm
def max_subarray_sum(arr):
    if len(arr) == 0:
        return 0

    max_ending_here = max_so_far = arr[0]

    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far
