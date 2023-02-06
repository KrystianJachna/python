def search(nums, target):
    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = int((L + R) / 2)

        if mid == target:
            return mid
        elif mid < target:
            L = mid + 1
        else:
            R = mid - 1
    return -1

nums = [-1,0,3,5,9,12]

print(search(nums, 9))