def binary_search(arr, res):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == res:
            return mid
        elif arr[mid] < res:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
res = 12
result = binary_search(arr, res)

if result != -1:
    print(f"{res} found in index {result}.")
else:
    print(f"{res} not found in the list.")
