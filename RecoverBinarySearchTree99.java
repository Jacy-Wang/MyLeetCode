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
    public void recoverTree(TreeNode root) {
        TreeNode[] pointer = new TreeNode[3];
        for (int i = 0; i < pointer.length; i++)
            pointer[i] = null;
        findNodes(root, null, pointer);
        if (pointer[2] == null) {
            swapNodes(pointer[0], pointer[1]);
        } else {
            swapNodes(pointer[0], pointer[2]);
        }
    }

    private void swapNodes(TreeNode n1, TreeNode n2) {
        int tmp = n1.val;
        n1.val = n2.val;
        n2.val = tmp;
    }

    private TreeNode findNodes(TreeNode root, TreeNode prev, TreeNode[] pointer) {
        if (root != null) {
            TreeNode node = findNodes(root.left, prev, pointer);
            if (node != null) {
                if (node.val >= root.val) {
                    if (pointer[0] == null) {
                        pointer[0] = node;
                        pointer[1] = root;
                    } else {
                        pointer[2] = root;
                    }
                }
            }
            return findNodes(root.right, root, pointer);
        }
        return prev;
    }
}
