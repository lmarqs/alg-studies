class Solution:
    def isValid(self, expression):
        dic = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for i in range(len(expression)):
            char = expression[i]

            if char in dic:
                stack.append(char)
            else:
                if len(stack) == 0 or char != dic[stack.pop()]:
                    return False

        return True
