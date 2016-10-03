def mergeSort(nums):
    tmp = nums[:]
    topDown(nums, tmp, 0, len(nums))
    print nums

def topDown(dest, src, start, end):
    if start == end - 1:
        return
    else:
        mid = (start + end) / 2
        topDown(dest, src, start, mid)
        topDown(dest, src, mid, end)
    i = start
    j = mid
    k = start
    while i < mid and j < end:
        if src[i] <= src[j]:
            dest[k] = src[i]
            i += 1
        else:
            dest[k] = src[j]
            j += 1
        k += 1
    while i < mid:
        dest[k] = src[i]
        k += 1
        i += 1
    while j < end:
        dest[k] = src[j]
        k += 1
        j += 1
    src[start : end] = dest[start : end]

def test():
    arr = [4,2,5,7,1,4,7,0]
    mergeSort(arr)
if __name__ == "__main__":
    test()
