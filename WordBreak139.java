public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
        /*if (s.length() == 0)
            return true;
        for (int i = 1; i <= s.length(); i++) {
            if (wordDict.contains(s.substring(0, i))) {
                if (wordBreak(s.substring(i), wordDict))
                    return true;
            }
        }
        return false;*/
    }
}
