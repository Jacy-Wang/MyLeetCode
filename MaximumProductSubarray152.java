public class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int maxProd = nums[0];
        int minProd = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int tmp = maxProd;
            maxProd = Math.max(Math.max(maxProd * nums[i], minProd * nums[i]), nums[i]);
            minProd = Math.min(Math.min(tmp * nums[i], minProd * nums[i]), nums[i]);
            res = Math.max(res, maxProd);
        }
        return res;
    }
}
