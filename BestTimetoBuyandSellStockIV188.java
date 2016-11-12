public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        int profit = 0;
        if (k > n / 2) {
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) {
                    profit += (prices[i] - prices[i - 1]);
                }
            }
            return profit;
        }
        int[] p = new int[2 * k + 1];
        for (int i = 0; i < p.length; i++)
            p[i] = Integer.MIN_VALUE;
        p[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = Math.min(i + 1, 2 * k); j > 0; j--) {
                int tmp = j % 2 == 0 ? prices[i] : -prices[i];
                p[j] = Math.max(p[j], p[j - 1] + tmp);
                profit = Math.max(profit, p[j]);
            }
        }
        return profit;
    }
}
