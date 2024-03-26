
# array MUST BE sorted

def binary_search(arr, left, right, value):
    mid = (left + right) // 2
    if arr[mid] > value:
        return binary_search(arr, left, mid - 1, value)
    elif arr[mid] < value:
        return binary_search(arr, mid + 1, right, value)
    elif arr[mid] == value:
        return mid
    else:
        return None


arr = [1, 2, 3, 4]
result = binary_search(arr, 0, len(arr) - 1, 2)
print(result)








