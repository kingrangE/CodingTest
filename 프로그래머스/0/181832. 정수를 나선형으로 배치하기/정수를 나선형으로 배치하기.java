class Solution {
    public int[][] solution(int n) {
        int x = 0;
        int y = 0;
        int dx = 0;
        int dy = 1;
        int count = 1;
        int [][] arr = new int[n][n];
        
        while(count<=n*n){
            arr[x][y] = count;
            int tmp_x = x+dx;
            int tmp_y = y+dy;
            if (tmp_x < n && tmp_x >= 0 && tmp_y < n && tmp_y >=0 && arr[tmp_x][tmp_y] == 0){
                    // 유효 범위 내에 있고, 다음 위치가 아직 채워지지 않았다면
                    x = tmp_x;
                    y = tmp_y;
                    //이동한 값으로 갱신
            }else{
                if (dx == 1 && dy == 0) {
                    dx = 0;
                    dy = -1;
                }else if(dx==0&&dy==1){
                    dx = 1;
                    dy = 0;
                }else if(dx == -1 && dy == 0){
                    dx = 0;
                    dy = 1;
                }else{
                    dx = -1;
                    dy = 0;
                }
                x = x + dx;
                y = y +dy;
            }    
            count++;
        }
        for (int i =0 ; i<n;i++){
            for (int j = 0; j<n; j++){
                System.out.printf("%d ",arr[i][j]);
            }
            System.out.println();
        }
        return arr;
        // return answer;
    }
}