class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        i = 0
        j = 0
        res = []
        while i < len(n1) and j < len(n2):
            if n1[i] == n2[j]:
                res.append(n1[i])
                i += 1
                j += 1
            elif n1[i] < n2[j]:
                i += 1
            else:
                j += 1
        return res
