/*
 * An O(1) space solution would be reusing the costs[] array to store r[], b[] and g[].
 */
public class PaintHouse {
	public int minCost(int[][] costs) {
		if (costs.length == 0)
			return 0;
		int[] r = new int[costs.length];
		int[] b = new int[costs.length];
		int[] g = new int[costs.length];
		r[0] = costs[0][0];
		b[0] = costs[0][1];
		g[0] = costs[0][2];
		for (int i = 1; i < costs.length; i++) {
			r[i] = Math.min(b[i - 1], g[i - 1]) + costs[i][0];
			b[i] = Math.min(r[i - 1], g[i - 1]) + costs[i][1];
			g[i] = Math.min(r[i - 1], b[i - 1]) + costs[i][2];
		}
		return Math.min(Math.min(r[costs.length - 1], b[costs.length - 1]), g[costs.length - 1]);
	}
}
