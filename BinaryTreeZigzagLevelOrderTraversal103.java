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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null)
            return res;
        Deque<MyTuple> dq = new ArrayDeque<MyTuple>();
        dq.addLast(new MyTuple(root, 0));
        ArrayList<Integer> arr = new ArrayList<>();
        int num = 0;
        while (!dq.isEmpty()) {
            MyTuple first = dq.removeFirst();
            TreeNode node = first.getNode();
            int nextNum = first.getLevel();
            if (num < nextNum) {
                if ((num & 1) == 0) {
                    ArrayList<Integer> tmp = new ArrayList<>(arr);
                    res.add(tmp);
                } else {
                    ArrayList<Integer> tmp = new ArrayList<>();
                    for (int i = arr.size() - 1; i >= 0; i--) {
                        tmp.add(arr.get(i));
                    }
                    res.add(tmp);
                }
                arr.clear();
                num = nextNum;
            }
            arr.add(node.val);
            if (node.left != null)
                dq.addLast(new MyTuple(node.left, num + 1));
            if (node.right != null)
                dq.addLast(new MyTuple(node.right, num + 1));
        }
        if ((num & 1) == 0) {
            ArrayList<Integer> tmp = new ArrayList<>(arr);
            res.add(tmp);
        } else {
            ArrayList<Integer> tmp = new ArrayList<>();
            for (int i = arr.size() - 1; i >= 0; i--) {
                tmp.add(arr.get(i));
            }
            res.add(tmp);
        }
        return res;
    }

    class MyTuple {
        private TreeNode node;
        private int level;

        public MyTuple (TreeNode node, int level) {
            this.node = node;
            this.level = level;
        }

        public TreeNode getNode () {
            return this.node;
        }

        public int getLevel() {
            return this.level;
        }
    }
}
