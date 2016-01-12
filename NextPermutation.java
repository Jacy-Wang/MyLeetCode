c class Solution {
    public void nextPermutation(int[] nums) {
        int index = -1;
        for (int i = nums.length - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                index = i - 1;
                break;
            }
        }
        if (index == -1) {
            Arrays.sort(nums);
        }
        else {
            int pos = 0;
            for (int i = nums.length - 1; i > index; i--) {
                if (nums[i] > nums[index]) {
                    pos = i;
                    break;
                }
            }
            int tmp = nums[index];
            nums[index] = nums[pos];
            nums[pos] = tmp;
            int left = index + 1;
            int right = nums.length - 1;
            while (left < right) {
                tmp = nums[left];
                nums[left] = nums[right];
                nums[right] = tmp;
                left++;
                right--;
            }
        }
    }
}
