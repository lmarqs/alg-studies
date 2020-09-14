class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        if A == B:
            count = {}
            for c in A:
                if c in count:
                    return True
                else:
                    count[c] = True
            return False

        diff_count = 0
        diff_a = ''
        diff_b = ''

        for i in range(len(A)):
            if A[i] == B[i]:
                continue

            diff_count += 1

            if diff_count == 1:
                diff_a, diff_b = A[i], B[i]
                continue

            if diff_a != B[i] or diff_b != A[i] or diff_count > 2:
                return False

        return diff_count == 2
