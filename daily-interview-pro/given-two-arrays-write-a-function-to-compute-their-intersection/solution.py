class Solution:
    # using a set of known numbers, time: O(N + M), space: O(2 min(N, M))
    def intersection1(self, nums1, nums2):
        known = set()
        intersection = set()
        i = 0

        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        for n in nums1:
            while i < len(nums2) and not n in known:
                known.add(nums2[i])
                i += 1

            if n in known:
                intersection.add(n)

        return list(intersection)

    # sorting the arrays, time: O(N log N + M log M), space: min(N, M)
    def intersection2(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        intersection = set()
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]

            if nums1[i] == nums2[j]:
                intersection.add(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1

        return list(intersection)
