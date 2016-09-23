public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0)
            return 0;
        int[] dp = new int[nums.length];
        int maxLen = 1;
        for (int i = 0; i < dp.length; i++)
            dp[i] = 1;
        for (int i = 0; i < dp.length - 1; i++) {
            for (int j = i + 1; j < dp.length; j++) {
                if (nums[i] < nums[j])
                    dp[j] = Math.max(dp[j], dp[i] + 1);
                maxLen = Math.max(dp[j], maxLen);
            }
        }
        return maxLen;
    }
}
