class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        // 통분하고 기약분수 만들기
        
        // 통분
        int total_denom = denom1 *denom2;
        int total_numer = denom1 * numer2 + denom2 * numer1;
        
        // 기약 분수 만들기 (반복문) -> 안 됨 (소인수 분해로 변경)
        int div = 2;
        while(div <= total_denom){
            if(total_denom%div == 0 && total_numer%div == 0){
                //둘다 나눠지면 나누기
                total_denom /= div;
                total_numer /= div;
                div = 2;
                continue;
            }
            div += 1;
        }
        
        int[]  answer = {total_numer,total_denom};
        return answer;
    }
}