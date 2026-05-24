

def binarySearch(arr , target):
    lo , hi = 0 ,len(arr)-1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid-1
        else:
            lo = mid + 1
    return -1

arr = [2, 5, 8, 12, 16, 23, 28, 33, 45, 52, 60, 71, 88]

value = binarySearch(arr , 5)
print("value found at ",value )