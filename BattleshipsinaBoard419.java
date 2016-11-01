public class Solution {
    public int countBattleships(char[][] board) {
        int res = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'X') {
                    if (isValid(i - 1, j) && board[i - 1][j] == 'X')
                        continue;
                    if (isValid(i, j - 1) && board[i][j - 1] == 'X')
                        continue;
                    res++;
                }
            }
        }
        return res;
    }

    private boolean isValid(int row, int col) {
        return row >= 0 && col >= 0;
    }
}
