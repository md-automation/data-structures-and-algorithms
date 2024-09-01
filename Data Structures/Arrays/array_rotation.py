def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # Handle if d > n
    return arr[d:] + arr[:d]

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotated_array = rotate_array(arr, d)
print(rotated_array)  # Output: [3, 4, 5, 6, 7, 1, 2]