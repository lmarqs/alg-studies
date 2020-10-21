def buy_and_sell(arr):
    if len(arr) == 0:
        return 0

    lower_value = arr[0]
    max_profit = 0

    for n in arr[1:]:
        lower_value = min(lower_value, n)
        max_profit = max(max_profit, n - lower_value)

    return max_profit
