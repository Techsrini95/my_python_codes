# bubble sort

nums = [5, 2, 3, 6, 7, 9, 8]


def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


sort(nums)

print(nums)

# selection sort

list = [5, 2, 4, 6, 7, 9, 11]


def sort_num(list):
    for i in range(len(list) - 1):
        minpos = i
        for j in range(i, 7):
            if list[i] < list[minpos]:
                minpos = i
    temp = nums[i]
    nums[i] = nums[minpos]
    nums[minpos] = temp


sort_num(list)
print(list)
