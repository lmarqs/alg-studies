from bisect import bisect_left

def two_sum(list, k):
  list.sort()

  for i in range(len(list)):
    target = k - list[i]
    j = bisect_left(list, target)
    if j != i and 0 <= j < len(list) and list[j] == target:
      return True

  return False