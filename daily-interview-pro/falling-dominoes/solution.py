import math


class Solution(object):

    def pushDominoes(self, dominoes):
        l = len(dominoes)
        forces = [0] * l

        i = 0

        while i < l:
            c = dominoes[i]

            if c == 'R':
                j = i + 1
                while j < l and dominoes[j] != 'L':
                    forces[j] += 1 / (j - i)
                    j += 1

                # optimization
                i = j
                continue


            if c == 'L':
                j = i - 1
                while j >= 0 and dominoes[j] != 'R':
                    forces[j] += 1 / (j - i)
                    j -= 1

            i += 1

        result = ''
        for i in range(l):
            f = forces[i]
            if f > 0:
                result += 'R'
            elif f < 0:
                result += 'L'
            else:
                result += dominoes[i]

        return result

