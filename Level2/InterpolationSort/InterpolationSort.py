def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = interpolation_search(arr, target)

if result != -1:
    print(f"{target} found at index {result}.")
else:
    print(f"{target} not found in the array.")
