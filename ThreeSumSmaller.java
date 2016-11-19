import java.util.Arrays;

public class ThreeSumSmaller {
	public int threeSumSmaller(int[] nums, int target) {
		Arrays.sort(nums);
		int res = 0;
		int tmp;
		int left;
		int right;
		for (int i = 0; i < nums.length; i++) {
			tmp = target - nums[i];
			left = i + 1;
			right = nums.length - 1;
			while (left < right) {
				if (nums[left] + nums[right] >= tmp) {
					right--;
				} else {
					res += (right - left);
					left++;
				}
			}
		}
		return res;
	}
	
	public static void main(String[] args) {
		int[] nums = new int[]{-2, 0, 1, 3};
		int target = 2;
		ThreeSumSmaller tss = new ThreeSumSmaller();
		System.out.println(tss.threeSumSmaller(nums, target));
	}
}
