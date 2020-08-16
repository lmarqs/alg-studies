def word_search(matrix, word):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if find_right(matrix, i, j, word) or find_down(matrix, i, j, word):
                return True

    return False


def find_right(matrix, i, j, word):
    if j + len(word) > len(matrix[i]):
        return False

    k = 0

    while k < len(word):
        if word[k] != matrix[i][j + k]:
            break
        k += 1

    return k == len(word)


def find_down(matrix, i, j, word):
    if i + len(word) > len(matrix):
        return False

    k = 0

    while k < len(word):
        if word[k] != matrix[i + k][j]:
            break
        k += 1

    return k == len(word)
