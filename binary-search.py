def search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left+right) // 2
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
    return -1


arr = [1,2,3,4,5,6,7,8,12,22,45,87,102]

print(search(arr,1))