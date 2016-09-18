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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0)
            return null;
        TreeNode root = new TreeNode(preorder[0]);
        int leftLen = 0;
        for(int i = 0; i < inorder.length; i++) {
            if (inorder[i] == preorder[0]) {
                leftLen = i;
                break;
            }
        }
        TreeNode left = buildTree(Arrays.copyOfRange(preorder, 1, 1 + leftLen), Arrays.copyOfRange(inorder, 0, leftLen));
        TreeNode right = buildTree(Arrays.copyOfRange(preorder, 1 + leftLen, preorder.length), Arrays.copyOfRange(inorder, 1 + leftLen, inorder.length));
        root.left = left;
        root.right = right;
        return root;
    }
}
