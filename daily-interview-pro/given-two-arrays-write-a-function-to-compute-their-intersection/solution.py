class Solution:
    def intersection(self, nums1, nums2):
        known = set()
        intersection = set()
        i = 0

        for n in nums1:
            while i < len(nums2) and not n in known:
                known.add(nums2[i])
                i += 1

            if n in known:
                intersection.add(n)

        return list(intersection)
