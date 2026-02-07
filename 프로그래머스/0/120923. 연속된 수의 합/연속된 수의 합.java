class Solution {
    public int[] solution(int num, int total) {
        // 가운데 값을 구해서 개수만큼 더해주면 
		int[] answer = new int[num];
		// Java에서 int 나누기는 무조건 몫 반환 (float 형변환 필요)
		int start_point = (int)Math.ceil((float)total/num) - (int)(num/2);
		for (int i = start_point; i < start_point + num; i++) {
			answer[i-start_point] = i;
		}
		return answer;
    }
}