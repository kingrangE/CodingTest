class Solution {
    public int solution(int[][] board) {
        //시간제한 딱히 고려할게 없음 ( N <=100 이기 때문에 1초 안에 무조건 돌아감 )
        int answer = (int) Math.pow(board.length,2);
		
		// 1번 돌리기 (O(N^2))
		for(int row = 0; row < board.length; row++) {
			for(int col = 0; col < board[row].length; col++) {
				if(board[row][col] == 1) {
					answer -= 1; // 지뢰있는 자리 빼
					for(int x = row-1; x <=row+1; x++) {
						for(int y = col-1; y<=col+1; y++) {
							if (x < board.length && x >= 0 
									&& y < board.length && y>=0 
									&& board[x][y] == 0) {
								//범위가 유효하고 지뢰 범위 안에 없거나 지뢰가 아니면
								answer -= 1;
								//지뢰 범위 안에 있으면 빼고 방문처
								board[x][y] = 2;
							}
						}
					}
				}		
			}
		}
        return answer;
    }
}