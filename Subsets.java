import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i <= nums.length; i++) {
        	getSubsets(new ArrayList<Integer>(), 0, i, res, nums);
        }
        return res;
    }
    
    public void getSubsets(List<Integer> arr, int start, int targetLength, List<List<Integer>> res, int[] nums) {
    	if (arr.size() == targetLength) {
    		res.add(new ArrayList<Integer>(arr));
    	}
    	else {
    		for (int i = start; i <= nums.length + arr.size() - targetLength; i++) {
    			arr.add(nums[i]);
    			getSubsets(arr, i + 1, targetLength, res, nums);
    			arr.remove(arr.size() - 1);
    		}
    	}
    }
}