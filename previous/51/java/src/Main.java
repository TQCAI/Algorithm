import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    int n = 0;
    List<List<String>> res;
    int[] queens;
    int[] col;
    int[] dg;
    int[] udg;

    public void dfs(int i) {
        if (i == n) {
            res.add(getBoard(queens));
        }
        for (int j = 0; j < n; j++) {
            int dgi = i - j + n;
            int udgi = i + j;
            if (col[j] != 1 && dg[dgi] != 1 && udg[udgi] != 1) {
                queens[i] = j;
                col[j] = dg[dgi] = udg[udgi] = 1;
                dfs(i + 1);
                col[j] = dg[dgi] = udg[udgi] = 0;
            }
        }
    }

    public List<String> getBoard(int[] queens) {
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }

    public List<List<String>> solveNQueens(int n) {
        this.n = n;
        res = new ArrayList<>();
        queens = new int[n];
        col = new int[n];
        dg = new int[n * 2];
        udg = new int[n * 2];
        dfs(0);
        return res;
    }
}


public class Main {
    public static void main(String[] args) {
        List<List<String>> boards = (new Solution()).solveNQueens(4);
        for (List<String> board : boards) {
            for (String row : board) {
                System.out.println(row);
            }
            System.out.println();
        }
    }
}
