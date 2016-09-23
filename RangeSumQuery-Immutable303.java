public class NumArray {

    private int[] nums;
    private int[] partialSum;

    public NumArray(int[] nums) {
        this.nums = nums;
        partialSum = new int[nums.length + 1];
        partialSum[0] = 0;
        for (int i = 1; i < partialSum.length; i++)
            partialSum[i] = partialSum[i - 1] + nums[i - 1];
    }

    public int sumRange(int i, int j) {
        return partialSum[j + 1] - partialSum[i];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
