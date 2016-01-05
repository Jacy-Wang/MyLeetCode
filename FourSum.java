import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
    List<List<Integer>> res = new ArrayList<List<Integer>>(); 
    Arrays.sort(nums);
    kSum(0, nums.length - 1, target, 4, new ArrayList<Integer>(), nums, res);
    return res;
    }
    
    void kSum(int start, int end, int target, int k, ArrayList<Integer> curArr, int[] nums, List<List<Integer>> res) {
        if (k == 2) {
            for (List<Integer> r : twoSum(start, end, target, curArr, nums)) {
            	res.add(r);
            }
        }
        else {
        	for (int i = start; i <= end - k + 1; i++) {
        		if (i == start || nums[i] > nums[i - 1]) {
        			curArr.add(nums[i]);
        			kSum(i + 1, end, target - nums[i], k - 1, curArr, nums, res);
        			curArr.remove(curArr.size() - 1);
        		}
        	}
        }
    }
    
    List<List<Integer>> twoSum(int start, int end, int target, ArrayList<Integer> curArr, int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        while (start < end) {
            if (nums[start] + nums[end] == target) {
                curArr.add(nums[start]);
                curArr.add(nums[end]);
                res.add(new ArrayList<Integer>(curArr));
                curArr.remove(curArr.size() - 1);
                curArr.remove(curArr.size() - 1);
                int j = start + 1;
                while (j < end && nums[j] == nums[start]) {
                	j++;
                }
                start = j;
                j = end - 1;
                while(j > start && nums[j] == nums[end]) {
                	j--;
                }
                end = j;
            }
            else if (nums[start] + nums[end] < target) {
            	start++;
            }
            else {
            	end--;
            }
        }
        return res;
    }
    
    public static void main(String[] args) {
    	int[] nums = new int[]{0,0,0,0};
    	Arrays.sort(nums);
    	ArrayList<List<Integer>> res = new ArrayList<>();
    	new FourSum().kSum(
    			0, nums.length - 1, 0, 4, new ArrayList<Integer>(), nums,
    			res);
    	System.out.println(res);
    }
}