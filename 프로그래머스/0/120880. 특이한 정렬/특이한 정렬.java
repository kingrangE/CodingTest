import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        Map<Integer,ArrayList<Integer>> num_map = new HashMap<>();
		TreeSet<Integer> num_set = new TreeSet<Integer>();
		ArrayList<Integer> answer = new ArrayList<>();
		for(int num : numlist) {
			// numlist에서 값을 꺼내 차이에 대한 map으로 저장
			int diff = Math.abs(num-n) ;
			// 없으면, ArrayList 생성하고 add, 있으면 그냥 add
			num_map.computeIfAbsent(diff,key->new ArrayList<Integer>()).add(num);
			num_set.add(diff); // 차이에 대한 값을 save
		}
		for(int num : num_set) {
			// 차이가 작은 것부터 빼서 결과에 추가
			ArrayList tmp = num_map.get(num);
			tmp.sort(Comparator.reverseOrder()); // 내림차순 정렬
			answer.addAll(tmp);
		}
		return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}