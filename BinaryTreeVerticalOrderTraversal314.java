// not tested, just compiled, not submitted.
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Pair {
    private TreeNode value;
    private int col;

    public Pair(TreeNode value, int col) {
        this.value = value;
        this.col = col;
    }

    public TreeNode getValue() {
        return this.value;
    }

    public int getCol() {
        return this.col;
    }
}

public class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        ArrayList<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;
        ArrayList<Pair> arr = new ArrayList<>();
        Pair rootPair = new Pair(root, 0);
        traverse(rootPair, arr);
        Pair[] tmp = arr.toArray(new Pair[0]);
        Arrays.sort(tmp, new Comparator<Pair>(){
                @Override
                public int compare(Pair a, Pair b) {
                    return a.getCol() - b.getCol();
                }
            });
        int prevCol = 0;
        ArrayList<Integer> lst = new ArrayList<>();
        for (int i = 0; i < tmp.length; i++) {
            if (i == 0) {
                lst.add(tmp[i].getValue().val);
                prevCol = tmp[i].getCol();
            } else {
                if (tmp[i].getCol() == prevCol) {
                    lst.add(tmp[i].getValue().val);
                } else {
                    res.add(lst);
                    lst.clear();
                    lst.add(tmp[i].getValue().val);
                    prevCol = tmp[i].getCol();
                }
            }
        }
        return res;
    }

    private void traverse(Pair rootPair, ArrayList<Pair> arr) {
        TreeNode v = rootPair.getValue();
        int col = rootPair.getCol();
        arr.add(rootPair);
        if (v.left != null)
            traverse(new Pair(v.left, col - 1), arr);
        if (v.right != null)
            traverse(new Pair(v.right, col + 1), arr);
    }
}
