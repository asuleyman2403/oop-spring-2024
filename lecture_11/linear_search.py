
def linear_search(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return value


result = linear_search([1, 2, 3, 4], 5)
print(result)


