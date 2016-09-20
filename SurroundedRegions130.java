class MyTuple {
    int row;
    int col;
    public MyTuple (int x, int y) {
        row = x;
        col = y;
    }
}
public class Solution {
    public void solve(char[][] board) {
        if (board.length != 0 && board[0].length != 0) {
            int m = board.length;
            int n = board[0].length;
            boolean[][] visited = new boolean[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    visited[i][j] = false;
                }
            }
            Deque<MyTuple> queue = new ArrayDeque<>();
            for (int i = 0; i < m; i++) {
                if (board[i][0] == 'O' && !visited[i][0]) {
                    queue.addLast(new MyTuple(i, 0));
                    visited[i][0] = true;
                }
                if (board[i][n - 1] == 'O' && !visited[i][n - 1]) {
                    queue.addLast(new MyTuple(i, n - 1));
                    visited[i][n - 1] = true;
                }
            }
            for (int j = 0; j < n; j++) {
                if (board[0][j] == 'O' && !visited[0][j]) {
                    queue.addLast(new MyTuple(0, j));
                    visited[0][j] = true;
                }
                if (board[m - 1][j] == 'O' && !visited[m - 1][j]) {
                    queue.addLast(new MyTuple(m - 1, j));
                    visited[m - 1][j] = true;
                }
            }
            while (!queue.isEmpty()) {
                MyTuple top = queue.removeFirst();
                MyTuple[] directions = new MyTuple[]{new MyTuple(0, 1), new MyTuple(0, -1), new MyTuple(1, 0), new MyTuple(-1, 0)};
                for (MyTuple e : directions) {
                    int r = e.row + top.row;
                    int c = e.col + top.col;
                    MyTuple neighbor = new MyTuple(r, c);
                    if (isValid(neighbor, m, n) && board[r][c] == 'O' && !visited[r][c]) {
                        queue.addLast(neighbor);
                        visited[r][c] = true;
                    }
                }
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == 'O' && !visited[i][j])
                        board[i][j] = 'X';
                }
            }
        }
    }

    private boolean isValid(MyTuple t, int m, int n) { 
        return (t.row >= 0 && t.row < m && t.col >= 0 && t.col < n);
    }
}
