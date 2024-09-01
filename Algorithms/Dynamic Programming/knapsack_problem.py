def knapsack(weight_limit, weights, values, n):
    if n == 0 or weight_limit == 0:
        return 0

    if weights[n-1] > weight_limit:
        return knapsack(weight_limit, weights, values, n-1)
    
    else:
        return max(
            values[n-1] + knapsack(weight_limit-weights[n-1], weights, values, n-1),
            knapsack(weight_limit, weights, values, n-1)
        )

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
weight_limit = 50
n = len(values)
print("Maximum value in Knapsack =", knapsack(weight_limit, weights, values, n))  # Output: Maximum value in Knapsack = 220
