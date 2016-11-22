import java.util.ArrayList;
import java.util.HashMap;

public class GraphValidTree {
	public static void main(String[] args) {
		int n = 5;
		int[][] edges = new int[][]{new int[]{0, 1}, new int[]{0, 2}, new int[]{0, 3}, new int[]{1, 4}};
		edges = new int[][]{new int[]{0, 1}, new int[]{1, 2}, new int[]{2, 3}, new int[]{1, 3}, new int[]{1, 4}};
		edges = new int[][]{new int[]{0, 1}, new int[]{1, 2}, new int[]{3, 4}};
		System.out.println(new GraphValidTree().validTree(n, edges));
	}
	
	public boolean validTree(int n, int[][] edges) {
		if (n == 0)
			return true;
		boolean[] visited = new boolean[n];
		for (int i = 0; i < n; i++) {
			visited[i] = false;
		}
		HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
		for (int i = 0; i < edges.length; i++) {
			fillMap(edges[i][0], edges[i][1], map);
			fillMap(edges[i][1], edges[i][0], map);
		}
		visited[0] = true;
		visit(0, visited, map, -1);
		for (int i = 0; i < n; i++) {
			if (!visited[i])
				return false;
		}
		return true;
	}
	
	public boolean visit(int node, boolean[] visited, HashMap<Integer, ArrayList<Integer>> map, int prev) {
		if (map.containsKey(node)) {
			ArrayList<Integer> neighbors = map.get(node);
			int neighbor;
			for (int i = 0; i < neighbors.size(); i++) {
				neighbor = neighbors.get(i);
				if (neighbor - prev != 0) {
					if (visited[neighbor]) {
						return false;
					}						
					else {
						visited[neighbor] = true;
						visit(neighbor, visited, map, node);
					}
				}
			}
			return true;
		}
		return false;
	}
	
	public void fillMap(int from, int to, HashMap<Integer, ArrayList<Integer>> map) {
		if (map.containsKey(from)) {
			map.get(from).add(to);
		} else {
			ArrayList<Integer> lst = new ArrayList<>();
			lst.add(to);
			map.put(from, lst);
		}
	}
}
