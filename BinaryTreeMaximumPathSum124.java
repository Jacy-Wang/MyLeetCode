/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxPathSum(TreeNode root) {
        int[] res = findPath(root, Integer.MIN_VALUE);
        return res[1];
    }

    private int[] findPath(TreeNode root, int globalMax) {
        int[] res = new int[2];
        if (root == null) {
            res[0] = 0;
            res[1] = globalMax;
        } else {
            int[] leftRes = findPath(root.left, globalMax);
            int[] rightRes = findPath(root.right, leftRes[1]);
            res[0] = Math.max(Math.max(leftRes[0] + root.val, rightRes[0] + root.val), root.val);
            res[1] = Math.max(Math.max(res[0], rightRes[1]), leftRes[0] + root.val + rightRes[0]);
        }
        return res;
    }
}
