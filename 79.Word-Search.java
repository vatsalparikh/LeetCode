class Solution {
    public boolean exist(char[][] board, String word) {

        if(board.length == 0 || word.length() == 0) return false;

        char[] wordChars = word.toCharArray();

        for(int row = 0; row < board.length; row++){
            for(int col = 0; col < board[0].length; col++){
                int wordCharPosition = 0;
                boolean[][] visited = new boolean[board.length][board[0].length];
                if(dfs(board, wordChars, visited, row, col, wordCharPosition)) return true;
            }
        }

        return false;
    }

    public boolean dfs(char[][] board, char[] wordChars, boolean[][] visited, int row, int col, int wordCharPosition){
            if(board[row][col] == wordChars[wordCharPosition]){
                visited[row][col] = true;
                if(wordCharPosition == wordChars.length - 1) return true;
                if(row < board.length - 1 && !visited[row+1][col] && dfs(board, wordChars, visited, row+1, col, wordCharPosition+1)) {
                    return true;
                }
                if(row > 0 && !visited[row-1][col] && dfs(board, wordChars, visited, row-1, col, wordCharPosition+1)){
                    return true;
                }
                if(col < board[0].length - 1 && !visited[row][col+1] && dfs(board, wordChars, visited, row, col+1, wordCharPosition+1)){
                    return true;
                }
                if(col >0 && !visited[row][col-1] && dfs(board, wordChars, visited, row, col-1, wordCharPosition+1)){
                    return true;
                }
                visited[row][col] = false;
            }
            return false;
    }
}
