def quickSort(nums, start, end):
    if end > start:
        p = partition(nums, start, end)
        quickSort(nums, start, p - 1)
        quickSort(nums, p + 1, end)

def partition(nums, start, end):
    val = nums[end]
    pos = start - 1
    for i in xrange(start, end):
        if nums[i] <= val:
            pos += 1
            swap(nums, pos, i)
    swap(nums, pos + 1, end)
    return pos + 1

def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

def test():
    nums = [4,2,5,2,5,7,2,1,0]
    quickSort(nums, 0, len(nums) - 1)
    print nums

if __name__ == "__main__":
    test()
