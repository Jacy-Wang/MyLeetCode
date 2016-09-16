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
    public boolean isValidBST(TreeNode root) {
        if (root == null)
            return true;
        ArrayList<Integer> val = new ArrayList<>();
        traverse(root, val);
        if (val.size() == 1)
            return true;
        for (int i = 1; i < val.size(); i++) {
            if (val.get(i) <= val.get(i - 1))
                return false;
        }
        return true;
    }

    private void traverse(TreeNode node, ArrayList<Integer> val) {
        if (node.left != null)
            traverse(node.left, val);
        val.add(node.val);
        if (node.right != null)
            traverse(node.right, val);
    }
}
