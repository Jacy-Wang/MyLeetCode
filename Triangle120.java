public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] prevMin = new int[n];
        int[] curMin = new int[n];
        prevMin[0] = triangle.get(0).get(0);
        findMin(triangle, n, 1, prevMin, curMin);
        int minimum = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (prevMin[i] < minimum) {
                minimum = prevMin[i];
            }
        }
        return minimum;
    }

    private void findMin(List<List<Integer>> triangle, int n, int level, int[] prevMin, int[] curMin) {
        if (level < n) {
            List<Integer> arr = triangle.get(level);
            for (int i = 0; i < arr.size(); i++) {
                if (i == 0) {
                    curMin[i] = prevMin[i] + arr.get(i);
                } else if (i == arr.size() - 1) {
                    curMin[i] = prevMin[i - 1] + arr.get(i);
                } else {
                    curMin[i] = Math.min(prevMin[i - 1], prevMin[i]) + arr.get(i);
                }
            }
            for (int i = 0; i < level + 1; i++) {
                prevMin[i] = curMin[i];
            }
            findMin(triangle, n, level + 1, prevMin, curMin);
        }
    }
}
