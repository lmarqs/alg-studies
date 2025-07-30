counter = 0


def num_ways(n, m):
    return num_ways_iterative(n, m)


def num_ways_recursive(n, m):
    global counter
    counter += 1

    if n <= 1 or m <= 1:
        return 1

    return num_ways(n - 1, m) + num_ways(n, m - 1)


def num_ways_iterative(n, m):
    global counter
    counter += 1

    matrix = [None] * n

    for i in range(n):
        matrix[i] = [None] * m

        for j in range(m):
            counter += 1

            if i == 0 or j == 0:
                matrix[i][j] = 1
                continue

            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[n - 1][m - 1]


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    counters = []
    for x in range(1, 13):
        counter = 0
        num_ways(x, x)
        counters.append(counter)

    plt.plot(counters)
    plt.show()
