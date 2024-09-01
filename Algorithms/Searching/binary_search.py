def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
print("Element is present at index", result)  # Output: Element is present at index 3
