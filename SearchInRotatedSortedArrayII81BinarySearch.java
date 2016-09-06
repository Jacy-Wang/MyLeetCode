// solve by binary search, worst case complexity is O(n)
// worst case example: find 0 in [1,1,1,1,1,1,1]
public class Solution {
    public boolean search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] == target)
                return true;
            else if (nums[mid] > nums[start]) {
                if (nums[start] <= target && target < nums[mid])
                    end = mid - 1;
                else
                    start = mid + 1;
            }
            else if (nums[mid] < nums[start]) {
                if (nums[mid] < target && target <= nums[end])
                    start = mid + 1;
                else
                    end = mid - 1;
            }
            else
                start++;
        }
        return false;
    }
}
