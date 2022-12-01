# linear search

pos = -1


def search(arr, n):
    i = 0

    while i < len(arr):
        if arr[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


arr = [5, 6, 8, 9, 6]

n = 8

if search(arr, n):
    print('found', pos + 1)
else:
    print('not found')

# Binary search

list = [2, 4, 3, 5, 8, 9, 0, 1]

n = 7

pos1 = -1


def searchb(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos1'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
            return False


if searchb(list, n):
    print('found at pos', pos1 + 1)
else:
    print('not found')
