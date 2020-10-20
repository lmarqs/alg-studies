class Solution():
    def fibonacci(self, n):
        b = 0
        a = 1
        for _ in range(1, n):
            a, b = a + b, a
        return a
