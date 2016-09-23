public class NumMatrix {

    int[][] matrix;
    int[][] partialSum;
    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;
        if (matrix.length > 0 && matrix[0].length > 0) {
            partialSum = new int[matrix.length][matrix[0].length + 1];
            for (int i = 0; i < partialSum.length; i++) {
                partialSum[i][0] = 0;
                for (int j = 1; j < partialSum[0].length; j++) {
                    partialSum[i][j] = partialSum[i][j - 1] + matrix[i][j - 1];
                } 
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int i = row1; i <= row2; i++) {
            sum += (partialSum[i][col2 + 1] - partialSum[i][col1]);
        }
        return sum;
    }
}


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix = new NumMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.sumRegion(1, 2, 3, 4);
