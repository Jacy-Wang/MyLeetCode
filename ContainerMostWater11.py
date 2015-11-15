class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        curMax = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > curMax:
                curMax = area
            if height[i] <= height[j]:
                i = i + 1
            elif height[i] > height[j]:
                j = j - 1
        return curMax
