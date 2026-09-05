#TOP-DOWN APPROACH

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

n = len(weights)

dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

def knapsack(i, capacity):
    if i == 0 or capacity == 0:
        return 0

    if dp[i][capacity] != -1:
        return dp[i][capacity]

    if weights[i - 1] <= capacity:
        dp[i][capacity] = max(
            values[i - 1] + knapsack(i - 1, capacity - weights[i - 1]),
            knapsack(i - 1, capacity)
        )
    else:
        dp[i][capacity] = knapsack(i - 1, capacity)

    return dp[i][capacity]

print("Maximum value:", knapsack(n, capacity))