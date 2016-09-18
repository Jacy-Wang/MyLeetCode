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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        TreeNode root = build(inorder, postorder, map, 0, inorder.length - 1, 0, postorder.length - 1);
        return root;
    }

    private TreeNode build(int[] inorder, int[] postorder, HashMap<Integer, Integer> map, int inLeft, int inRight, int postLeft, int postRight) {
        if (inLeft > inRight || postLeft > postRight)
            return null;
        TreeNode root = new TreeNode(postorder[postRight]);
        int leftLen = map.get(postorder[postRight]);
        TreeNode left = build(inorder, postorder, map, inLeft, leftLen - 1, postLeft, postLeft - inLeft + leftLen - 1);
        TreeNode right = build(inorder, postorder, map, leftLen + 1, inRight, postRight - inRight + leftLen, postRight - 1);
        root.left = left;
        root.right = right;
        return root;
    }
}
