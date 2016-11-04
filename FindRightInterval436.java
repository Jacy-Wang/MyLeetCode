/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */

class Tuple {
    private Interval interval;
    private int index;

    public Tuple(Interval interval, int index) {
        this.interval = interval;
        this.index = index;
    }

    public Interval getInterval() {
        return this.interval;
    }

    public int getIndex() {
        return this.index;
    }
}

public class Solution {
    public int[] findRightInterval(Interval[] intervals) {
        Tuple[] tuples = new Tuple[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            tuples[i] = new Tuple(intervals[i], i);
        }
        Arrays.sort(tuples, new Comparator<Tuple>(){
            @Override
            public int compare(Tuple t1, Tuple t2) {
                return t1.getInterval().start - t2.getInterval().start;
            }
        });
        int[] res = new int[intervals.length];
        for (int i = 0; i < tuples.length; i++) {
            int curEnd = tuples[i].getInterval().end;
            int idx = tuples[i].getIndex();
            int left = i + 1;
            int right = tuples.length - 1;
            boolean found = false;
            while (left <= right) {
                int mid = (left + right) / 2;
                Interval curInterval = tuples[mid].getInterval();
                if (curInterval.start == curEnd) {
                    res[idx] = tuples[mid].getIndex();
                    found = !found;
                    break;
                } else if (curInterval.start < curEnd) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            if (!found)
                res[idx] = (left > i && left < tuples.length) ? tuples[left].getIndex() : -1;
        }
        return res;
    }
}
