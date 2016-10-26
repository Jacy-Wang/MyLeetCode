public class Solution {
    public boolean canCross(int[] stones) {
        if (stones.length == 1)
            return true;
        if (stones[1] != 1)
            return false;
        if (stones.length == 2)
            return true;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < stones.length; i++) {
            map.put(stones[i], i);
        }
        HashMap<Integer, HashSet<Integer>> src = new HashMap<>();
        HashSet<Integer> set = new HashSet<>();
        set.add(0);
        src.put(1, set);
        for (int i = 1; i < stones.length; i++) {
            if (src.containsKey(i)) {
                for (int s : src.get(i)) {
                    int step = stones[i] - stones[s];
                    for (int j = -1; j < 2; j++) {
                        if (step + j > 0) {
                            int pos = stones[i] + step + j;
                            if (map.containsKey(pos)) {
                                int idx = map.get(pos);
                                if (idx == stones.length - 1)
                                    return true;
                                if (src.containsKey(idx)) {
                                    src.get(idx).add(i);
                                } else {
                                    HashSet<Integer> curSet = new HashSet<>();
                                    curSet.add(i);
                                    src.put(idx, curSet);
                                }
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
}

// recursion TLE
public class Solution {
    public boolean canCross(int[] stones) {
        if (stones.length == 1)
            return true;
        if (stones[1] != 1)
            return false;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < stones.length; i++) {
            map.put(stones[i], i);
        }
        return jump(stones, 0, 0, map);
    }

    private boolean jump(int[] stones, int curStone, int prevUnits, HashMap<Integer, Integer> map) {
        if (curStone == stones.length - 1)
            return true;
        for (int i = -1; i < 2; i++) {
            if (prevUnits + i > 0) {
                if (map.containsKey(prevUnits + i + stones[curStone])) {
                    if (jump(stones, map.get(prevUnits + i + stones[curStone]), prevUnits + i, map))
                        return true;
                }
            }
        }
        return false;
    }
}

