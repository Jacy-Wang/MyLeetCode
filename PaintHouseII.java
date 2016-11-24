
public class PaintHouseII {
	public int minCost(int[][] costs) {
		if (costs.length == 0 || costs[0].length == 0)
			return 0;
		int min = Integer.MAX_VALUE;
		int secondMin = min;
		int idx = -1;
		for (int i = 0; i < costs.length; i++) {
			int a = Integer.MAX_VALUE;
			int b = a;
			int cur = -1;
			for (int j = 0; j < costs[i].length; j++) {
				int v = (j == idx ? secondMin : min) + costs[i][j];
				if (v < a) {
					b = a;
					a = v;
					cur = j;
				} else if (v < b) {
					b = v;
				}
			}
			min = a;
			secondMin = b;
			idx = cur;
		}
		return min;
	}
}
