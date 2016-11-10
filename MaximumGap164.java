public class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2)
            return 0;
        int maxNum = Integer.MIN_VALUE;
        int minNum = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            maxNum = Math.max(maxNum, nums[i]);
            minNum = Math.min(minNum, nums[i]);
        }
        if (maxNum == minNum)
            return 0;
        int bucketSize = (int) Math.ceil(1.0 * (maxNum - minNum) / (nums.length - 1));
        int bucketNum = (maxNum - minNum) / bucketSize + 1;
        int[] maxB = new int[bucketNum];
        int[] minB = new int[bucketNum];
        int[] cnt = new int[bucketNum];
        for (int i = 0; i < bucketNum; i++) {
            maxB[i] = Integer.MIN_VALUE;
            minB[i] = Integer.MAX_VALUE;
            cnt[i] = 0;
        }
        for (int i = 0; i < nums.length; i++) {
            int idx = (nums[i] - minNum) / bucketSize;
            cnt[idx]++;
            maxB[idx] = Math.max(maxB[idx], nums[i]);
            minB[idx] = Math.min(minB[idx], nums[i]);
        }
        int maxGap = 0;
        int i = 0;
        while (i < bucketNum && cnt[i] == 0) {
            i++;
        }
        int prevIdx = i;
        for (int j = i + 1; j < bucketNum; j++) {
            if (cnt[j] == 0)
                continue;
            maxGap = Math.max(maxGap, minB[j] - maxB[prevIdx]);
            prevIdx = j;
        }
        return maxGap;
    }
}
