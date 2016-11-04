/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public int eraseOverlapIntervals(Interval[] intervals) {
        Arrays.sort(intervals, new Comparator<Interval>(){
            @Override
            public int compare(Interval i1, Interval i2) {
                if (i1.end == i2.end) {
                    return i1.start - i2.start;
                } else {
                    return i1.end - i2.end;
                }
            }
        });
        int curEnd = Integer.MIN_VALUE;
        int validNum = 0;
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i].start >= curEnd) {
                validNum++;
                curEnd = intervals[i].end;
            }
        }
        return intervals.length - validNum;
    }
}
