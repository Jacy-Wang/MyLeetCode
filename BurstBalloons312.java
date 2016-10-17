public class Solution {
    public int maxCoins(int[] nums) {
        int l = nums.length;
        int[][] coins = new int[l + 2][l + 2];
        for (int i = 0; i < l + 2; i++) {
            for (int j = 0; j < l + 2; j++) {
                coins[i][j] = 0;
            }
        }
        int leftNum = 1;
        int rightNum = 1;
        for (int k = 2; k < l + 2; k++) {
            for (int left = 0; left < l + 2 - k; left++) {
                for (int m = left + 1; m < left + k; m++) {
                    if (left == 0) {
                        leftNum = 1;
                    } else {
                        leftNum = nums[left - 1];
                    }
                    if (left + k == l + 1) {
                        rightNum = 1;
                    } else {
                        rightNum = nums[left + k - 1];
                    }
                    coins[left][left + k] = Math.max(coins[left][left + k], coins[left][m] + coins[m][left + k] + leftNum * nums[m - 1] * rightNum);
                }
            }
        }
        return coins[0][l + 1];
    }
}
