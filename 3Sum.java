public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        //HashSet<ArrayList<Integer>> set = new HashSet<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || nums[i] > nums[i - 1]) {
                int curSum = nums[i];
                int left = i + 1;
                int right = nums.length - 1;
                while (left < right) {
                    if (nums[left] + nums[right] == -curSum) {
                        ArrayList<Integer> tmp = new ArrayList<>();
                        tmp.add(nums[i]);
                        tmp.add(nums[left]);
                        tmp.add(nums[right]);
                        res.add(tmp);
                        int j = left + 1;
                        while (j < right && nums[j] == nums[left]){
                            j++;
                        }
                        left = j;
                        j = right - 1;
                        while (j > left && nums[j] == nums[right]){
                            j--;
                        }
                        right = j;
                    }
                    else if (nums[left] + nums[right] > -curSum) {
                        right--;
                    }
                    else {
                        left++;
                    }
                }
            }
        }
        return res;
    }
}
