def binary_search(arr, target):
    if target < arr[0]:
        return 0, arr[0]
    if target > arr[-1]:
        return 0, None
    left, right = 0, len(arr) - 1
    i = 0
    while left <= right:
        i+=1
        mid = left + (right - left) // 2
        if arr[mid-1] < target <= arr[mid]:
            return i, arr[mid]
        elif arr[mid-1] <= target < arr[mid]:
            return i, arr[mid-1]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return i, None