public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums.length == 0)
            return 0;
        int i = 0;
        int j = 0;
        int curSum = 0;
        int minLen = Integer.MAX_VALUE;
        while (j < nums.length) {
            if (curSum < s) {
                curSum += nums[j];
                j++;
            } else {
                minLen = Math.min(minLen, j - i);
                if (minLen == 1)
                    return minLen;
                curSum -= nums[i];
                i++;
            }
        }
        while (curSum >= s) {
            minLen = Math.min(minLen, j - i);
            curSum -= nums[i];
            i++;
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
