
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public int func(int record) {
        if (record == 0)
            return 1;
        else if (record == 1)
            return 2;
        return 0;
    }

    public int solution(int[] recordA, int[] recordB) {

        int cnt = 0;
        for (int i = 0; i < recordA.length; i++) {
            if (recordA[i] == recordB[i]) // 비겼을 경우
                continue;
            else if (recordA[i] == func(recordB[i])) // 이겼을 경우
                cnt = cnt + 3;
            else { // 졌을 경우
                if (cnt < 1) // 계단 제일 아래에 있을 경우
                    continue;
                cnt = cnt - 1;
            }
        }
        return cnt;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        int[] recordA = { 2, 0, 0, 0, 0, 0, 1, 1, 0, 0 };
        int[] recordB = { 0, 0, 0, 0, 2, 2, 0, 2, 2, 2 };
        int ret = sol.solution(recordA, recordB);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");

    }
}