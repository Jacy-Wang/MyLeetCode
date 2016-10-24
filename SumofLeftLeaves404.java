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
    public int sumOfLeftLeaves(TreeNode root) {
        return getSum(root, false);
    }

    private int getSum(TreeNode root, boolean isLeftChild) {
        if (root == null)
            return 0;
        if (root.left == null && root.right == null) {
            if (isLeftChild)
                return root.val;
            return 0;
        }
        int s = 0;
        if (root.left != null)
            s += getSum(root.left, true);
        if (root.right != null)
            s += getSum(root.right, false);
        return s;
    }
}
