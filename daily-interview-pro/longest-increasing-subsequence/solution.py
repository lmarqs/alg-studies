def longest_increasing_subsequence(arr):
    if len(arr) <= 1:
        return len(arr)

    longest_subsequences = [1] * arr

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                longest_subsequences[i] = max(longest_subsequences[i], longest_subsequences[j] + 1)

    return max(longest_subsequences)
