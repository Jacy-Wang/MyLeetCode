public class Solution {
    public List<int[]> pacificAtlantic(int[][] matrix) {
        ArrayList<int[]> res = new ArrayList<>();
        if (matrix.length == 0 || matrix[0].length == 0)
            return res;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] d = new int[][]{new int[]{0, -1}, new int[]{0, 1}, new int[]{-1, 0}, new int[]{1, 0}};
        boolean[][] pacific = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    pacific[i][j] = true;
                } else {
                    pacific[i][j] = false;
                }
            }
        }
        boolean[][] atlantic = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == m - 1 || j == n - 1) {
                    atlantic[i][j] = true;
                } else {
                    atlantic[i][j] = false;
                }
            }
        }
        for (int j = 0; j < n; j++) {
            flow(matrix, pacific, d, 0, j, m, n);
            flow(matrix, atlantic, d, m - 1, j, m, n);
        }
        for (int i = 1; i < m; i++) {
            flow(matrix, pacific, d, i, 0, m, n);
        }
        for (int i = 0; i < m - 1; i++) {
            flow(matrix, atlantic, d, i, n - 1, m, n);
        }

        int[] tmp;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    tmp = new int[]{i, j};
                    res.add(tmp);
                }
            }
        }
        return res;
    }

    private void flow(int[][] matrix, boolean[][] ocean, int[][] d, int i, int j, int m, int n) {
        int[] neighbor;
        for (int[] direction : d) {
            neighbor = new int[]{i + direction[0], j + direction[1]};
            if (isValid(neighbor[0], neighbor[1], m, n) && matrix[neighbor[0]][neighbor[1]] >= matrix[i][j]) {
                if (!ocean[neighbor[0]][neighbor[1]]) {
                    ocean[neighbor[0]][neighbor[1]] = true;
                    flow(matrix, ocean, d, neighbor[0], neighbor[1], m, n);
                }
            }
        }        
    }

    private boolean isValid(int i, int j, int m, int n) {
        return i >= 0 && i < m && j >= 0 && j < n;
    }
}
