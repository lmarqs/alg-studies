class Solution:
    def getRange(self, arr, target):
        head = -1
        tail = -1

        if len(arr) > 0:
            tail = self.findLowestIndex(arr, target)
            head = self.findHighestIndex(arr, target)

        return [tail, head]

    def findLowestIndex(self, arr, target):
        i = 0
        j = len(arr) - 1

        while i < j - 1:
            m = (i + j) // 2
            if arr[m] < target:
                i = m + 1
            else:
                j = m

        if arr[i] == target:
            return i

        if arr[j] == target:
            return j

        return -1

    def findHighestIndex(self, arr, target):
        i = 0
        j = len(arr) - 1

        while i < j - 1:
            m = (i + j) // 2
            if arr[m] > target:
                j = m - 1
            else:
                i = m

        if arr[j] == target:
            return j

        if arr[i] == target:
            return i

        return -1
