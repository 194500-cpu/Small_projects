import bisect

def binary_search(arr,target):
    if len(arr) == 0:
        return -1
    left = 0
    right = len(arr)

    while left+1 < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid


    if arr[left] == target:
        return left

    return -1


def main():
    arr = [1,4,2894,23834,139, 8293,291,9]
    arr.sort()
    x = 3
    index = binary_search(arr, x)
    print(index)
main()

