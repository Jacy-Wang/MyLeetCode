public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        ArrayList<ArrayList<Integer>> p = new ArrayList<>();
        for (int i = 0; i < people.length; i++) {
            ArrayList<Integer> cur = new ArrayList<>();
            cur.add(people[i][0]);
            cur.add(people[i][1]);
            cur.add(people[i][1]);
            p.add(cur);
        }
        int[][] res = new int[people.length][2];
        int cnt = 0;
        int minIdx = 0;
        int minVal;
        while (p.size() > 0) {
            minVal = Integer.MAX_VALUE; 
            for (int i = 0; i < p.size(); i++) {
                if (p.get(i).get(2) == 0 && p.get(i).get(0) < minVal) {
                    minIdx = i;
                    minVal = p.get(i).get(0);
                }
            }
            int[] cur = new int[2];
            cur[0] = minVal;
            cur[1] = p.get(minIdx).get(1);
            res[cnt++] = cur;
            p.remove(minIdx);
            for (int i = 0; i < p.size(); i++) {
                if (p.get(i).get(0) <= minVal) {
                    p.get(i).set(2, p.get(i).get(2) - 1);
                }
            }
        }
        return res;
    }
}
