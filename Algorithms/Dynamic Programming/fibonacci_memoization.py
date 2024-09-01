def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Example usage
n = 10
print(f"Fibonacci number at position {n} is {fibonacci(n)}")  # Output: Fibonacci number at position 10 is 55
