class Pair {
    private String s;
    private double val;

    public Pair(String s, double val) {
        this.s = s;
        this.val = val;
    }

    public String getStr() {
        return this.s;
    }

    public double getVal() {
        return this.val;
    }
}

public class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        HashMap<String, ArrayList<Pair>> table = new HashMap<>();
        for (int i = 0; i < equations.length; i++) {
            if (!table.containsKey(equations[i][0])) {
                ArrayList<Pair> pairs = new ArrayList<>();
                pairs.add(new Pair(equations[i][1], values[i]));
                table.put(equations[i][0], pairs);
            } else {
                table.get(equations[i][0]).add(new Pair(equations[i][1], values[i]));
            }
            if (!table.containsKey(equations[i][1])) {
                ArrayList<Pair> pairs = new ArrayList<>();
                pairs.add(new Pair(equations[i][0], 1.0 / values[i]));
                table.put(equations[i][1], pairs);
            } else {
                table.get(equations[i][1]).add(new Pair(equations[i][0], 1.0 / values[i]));
            }
        }
        double[] res = new double[queries.length];
        for (int i = 0; i < queries.length; i++) {
            res[i] = -1.0;
            if (table.containsKey(queries[i][0]))
                find(queries[i][0], queries[i][1], new HashMap<String, Integer>(), 1.0, table, i, res);
        }
        return res;
    }

    private void find(String start, String end, HashMap<String, Integer> path, double curVal, HashMap<String, ArrayList<Pair>> table, int pos, double[] res) {
        if (start.equals(end)) {
            res[pos] = curVal * 1.0;
        } else {
            if (table.containsKey(start)) {
                for (Pair pair : table.get(start)) {
                    String node = pair.getStr();
                    if (!path.containsKey(node)) {
                        path.put(node, 1);
                        find(node, end, path, curVal * pair.getVal(), table, pos, res);
                        path.remove(node);
                    }
                    if (res[pos] != -1.0)
                        return;
                }
            }
        }
    }
}
