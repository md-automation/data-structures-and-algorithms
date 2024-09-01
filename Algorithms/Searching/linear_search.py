def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10
result = linear_search(arr, x)
print("Element is present at index", result)  # Output: Element is present at index 3
