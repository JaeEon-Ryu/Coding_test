
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    int solution(int[] prices) {
        int inf = 1000000001;
        int tmp = inf;
        int answer = -inf;
        for (int price : prices) {
            if (tmp != inf)
                answer = Math.max(answer, price - tmp);
            tmp = Math.min(tmp, price);
        }
        return answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        int[] prices1 = { 1, 2, 3 };
        int ret1 = sol.solution(prices1);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");

        int[] prices2 = { 3, 1 };
        int ret2 = sol.solution(prices2);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");
    }
}