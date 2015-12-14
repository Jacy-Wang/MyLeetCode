class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not list:
            return 0
        start = 0
        end = len(citations) - 1
        while start <= end:
            mid = (start + end) / 2
            if len(citations) - mid == citations[mid]:
                return citations[mid]
            elif len(citations) - mid > citations[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return len(citations) - start
